import requests
import json

invalid_status_code = [400, 401, 402, 403, 404, 500, 501, 502, 503, 504]

put_body_content = ['''{
  "updateAttributeRefinements": [
    {
      "attributeNameId": null,
      "refinement": "YES",
      "attributeValueId": "1222157"
    },
    {
      "attributeNameId": "19611",
      "subcategoryId": "22421",
      "attributeValueId": "1222158",
      "refinement": "YES"
    },
    {
      "attributeNameId": "19611",
      "subcategoryId": "22421",
      "attributeValueId": "1222158",
      "refinement": "NO"
    },
    {
      "attributeNameId": "19611",
      "subcategoryId": "22421",
      "attributeValueId": "1222154",
      "refinement": "YES_NO",
      "recordUpdated": 1
    },
    {
      "attributeNameId": "19611",
      "subcategoryId": "22421",
      "attributeValueId": "1222155",
      "refinement": "YES",
      "recordUpdated": 1
    }
  ]
}
''']

def put_validation(body):
    print('Put Request Status and Request')
    connection = 'http://attributews-latte.test.overstock.com:20550/attributeValue/save'
    headers = {"content-type":"application/json"}
    req = requests.put(connection, data = body, headers = headers)
    json_data = req.text
    print('Status Code : ', req.status_code)
    if req.status_code in invalid_status_code:
        print('Invalid put request - ', req.status_code)
    else:    
        req_json_data = json.loads(str(json_data))
        update_attribute_refinement = req_json_data["updateAttributeRefinements"]
        print(update_attribute_refinement)
        print (json.dumps(req_json_data, indent=4))
        for attributes in update_attribute_refinement:
            print('Refinements : ', attributes['refinement'])
            if attributes['subcategoryId'] is None:
                print ('Subcat do not exist')
            else:
                print('Subcat_ID : ', attributes['subcategoryId'])
            print('Attribute_value_id : ', attributes['attributeValueId'])
            
for test_content in put_body_content:
    put_validation(test_content)
