import requests
import json
invalid_status_code = [401, 402, 403, 404, 500, 501, 502, 503, 504]
connection_latte = 'http://attributews-latte.test.overstock.com:20550/attributeValue'
connection_dogfood = 'http://attributews-dogfood.test.overstock.com:20550/attributeValue'
headers = {"content-type":"application/json"}
put_body_content = ['''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "refinement": "YES", "attributeValueId": "1222157"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19630", "subcategoryId": "14588", "attributeValueId": "1223229", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "3583", "subcategoryId": "20736", "attributeValueId": "2815728", "refinement": "NO"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "20766", "subcategoryId": "20623", "attributeValueId": "1285727", "refinement": "YES_NO"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19665", "subcategoryId": "23424", "attributeValueId": "2841378", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19614", "subcategoryId": "20473", "attributeValueId": "2841378", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": null, "subcategoryId": null, "attributeValueId": null, "refinement": null}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "0", "subcategoryId": "22421", "attributeValueId": "1222155", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "29451", "attributeValueId": "1222155", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "attributeValueId": "1155", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "attributeValueId": "1222155", "refinement": "YS"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19@#611", "subcategoryId": "22421", "attributeValueId": "1222155", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22fd421", "attributeValueId": "1222155", "refinement": "YES"}]}''',
'''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "attributeValueId": "122215500000000000000000000000000000000000000000000000000000000000000000000000000000000000000", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "attributeValueId": "1222155", "refinement": "Y"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "attributeValueId": "1222155", "refinement": "N"}]}''',
                    '''{"updateAttributeRefinements": [{"subcategoryId": "29451", "attributeValueId": "1222155", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "attributeValueId": "1222155", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421","refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "attributeValueId": "1222155"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": null, "subcategoryId": "22421", "attributeValueId": "1222155", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": null, "attributeValueId": "1222155", "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "attributeValueId": null, "refinement": "YES"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": "19611", "subcategoryId": "22421", "attributeValueId": "1222155", "refinement": null}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId": , "subcategoryId": "22421", "refinement": "YES", "attributeValueId": "1222157"}]}''',
                    '''{"updateAttributeRefinements": [{"attributeNameId":"" , "subcategoryId": "22421", "refinement": "YES", "attributeValueId": "1222157"}]}''']

def put_validation(body):
    print('***Put Request Status***')
    req = requests.put(connection_dogfood, data = body, headers = headers)
    json_data = req.text
    if req.status_code in invalid_status_code:
        print('Invalid put request - ', req.status_code)
        print(req.content)
    elif req.status_code == 400:
        print('Status Code : ', req.status_code)
        print("Expected status value, if requested parameters are incorrect")
        print(req.content)   
    else:
        print('Status Code : ', req.status_code)
        req_json_data = json.loads(str(json_data))
        update_attribute_refinement = req_json_data["updateAttributeRefinements"]
        #print (json.dumps(req_json_data, indent=4))
        for attributes in update_attribute_refinement:
            print('Refinements : ', attributes['refinement'])
            if attributes['subcategoryId'] is None:
                print ('Subcat do not exist')
            else:
                print('Subcat_ID : ', attributes['subcategoryId'])
            print('Attribute_value_id : ', attributes['attributeValueId'])
            if attributes['recordUpdated'] != True:
                print('Record has not been updated successfully ---',attributes['recordUpdated'] )
            else:
                print('record updated : ', attributes['recordUpdated'])            

for test_content in put_body_content:
    print(test_content)
    put_validation(test_content)
