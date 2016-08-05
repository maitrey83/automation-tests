import urllib
import requests
import json
invalid_status_code = [400, 401, 402, 403, 404, 500, 501, 502, 503, 504]
connection_latte = 'http://attributews-latte.test.overstock.com:20550/attributeValue/query'
connection_dogfood = 'http://attributews-latte.test.overstock.com:20550/attributeValue/query'
headers = {"content-type":"application/json"}
post_body_content = ['''{"attributeNameId":19611, "subcategoryIdList":[2030], "refinement":"YES"}''',
                     '''{"attributeNameId":19611, "subcategoryIdList":[2747], "refinement":"YES"}''',
                     '''{"attributeNameId":20766, "subcategoryIdList":[20696], "refinement":"NO"}''',
                     '''{"attributeNameId":19614, "subcategoryIdList":[6641], "refinement":"YES_NO"}''',
                     '''{"attributeNameId":19614, "subcategoryIdList":[6641, 1874, 1937, 2529], "refinement":"YES"}''',
                     '''{"attributeNameId":19630, "subcategoryIdList":[14471, 14525, 20541, 24877, 27728], "refinement":"NO"}''',
                     '''{"attributeNameId":19665, "subcategoryIdList":[2023,2739,3244,6404,6425,12130,12142], "refinement":"YES_NO"}''',
                     '''{"attributeNameId":null, "subcategoryIdList":null, "refinement":null}''',
                     '''{"attributeNameId":1961#*%$^a1, "subcategoryIdList":2030, "refinement":"YES"}''',
                     '''{"attributeNameId":19611, "subcategoryIdList":20a$%*730, "refinement":"YES"}''',
                     '''{"attributeNameId":19611, "subcategoryIdList":2030, "refinement":"Y   ES"}''',
                     '''{"attributeNameId":19611, "subcategoryIdList":2030, "refinement":"YDES"}''',
                     '''{"attributeNameId":19611, "subcategoryIdList":2030, "refinement":"Y@ES"}''',
                     '''{"attributeNameId":1961111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111, "subcategoryIdList":2030, "refinement":"Y@ES"}''',
                     '''{"attributeNameId":19611, "subcategoryIdList":203000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, "refinement":"Y@ES"}''',
                     '''{"attributeNameId":19611, "subcategoryIdList":2030, "refinement":"NO_YES"}'''
                    ]

invalid_status_code = [400, 401, 402, 403, 404, 500, 501, 502, 503, 504]
def post_validation(body):
    print('Post Request Status and Request')
    req = requests.post(connection_dogfood, data = body, headers = headers)
    json_data = req.text    
    #print('Status Code : ', req.status_code)
    if req.status_code in invalid_status_code:
        print('Invalid Status Code', req.status_code)
        print(req.content)
    else:
        req_json_data = json.loads(str(json_data))
        #print(req_json_data)
        #subcat = req_json_data["attributeValuesDTOs"][0]
        #print (json.dumps(req_json_data, indent=4))
        attribute_name_id = req_json_data["attributeNameId"]
        atr_value = req_json_data["attributeValuesDTOs"]
        print('Counts : ', len(atr_value))
        #print(atr_value)
        print('Attribute Name Id : ', attribute_name_id)
        for attributes in atr_value:
            #print('Refinements : ', attributes['refinement'])
            #print('Subcat_ID : ', attributes['subCategoryId'])
            #print('last_modified_by: ' , attributes['lastModifiedBy'])
            print('Attribute_value : ', attributes['attributeValue'])
            #print('Attribute_value_id : ', attributes['attributeValueId'])
    
for test_post_content in post_body_content:
    print(test_post_content)
    post_validation(test_post_content)
    

