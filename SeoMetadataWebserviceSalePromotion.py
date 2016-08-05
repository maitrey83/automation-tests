import requests
import json
invalid_status_code = [400, 401, 402, 403, 404, 500, 501, 502, 503, 504]
latte = 'http://seometadataservice-latte.test.overstock.com/metadata?taxonomyLevel=DEPARTMENT&taxonomyId=4'
dogfood = '''http://seometadataservice-dogfood.test.overstock.com/metadata?taxonomyLevel=DEPARTMENT&taxonomyId=4'''
dev = '''http://seometadataservice-lattedev.dev.overstock.com/metadata?taxonomyLevel=DEPARTMENT&taxonomyId=4'''
headers = {"content-type":"application/json"}
post_body_content = ['''{"objectType" : "TaxonomyPageMetaDataContext", "childTaxonomies": null, "currentTaxonomy": "Wall Decor", "parentTaxonomy": "Nursery Decor", "selectedRefinementList": null,"saleDescription": "Extra 15% off","allRefinements": null}''',
                     '''{"objectType" : "TaxonomyPageMetaDataContext", "childTaxonomies": null, "currentTaxonomy": "Wall Decor", "parentTaxonomy": "Nursery Decor", "selectedRefinementList": null,"saleDescription": null,"allRefinements": null}''',
                     '''{"objectType" : "TaxonomyPageMetaDataContext", "childTaxonomies": null, "currentTaxonomy": "Garden-Patio", "parentTaxonomy": "Home & Garden", "selectedRefinementList": null,"saleDescription": "Something%^& 342452 Off","allRefinements": null}''']

def post_validation(body):
    req = requests.post(dogfood, data=body, headers = headers)
    json_data = req.text
    
    #print(req.status_code)
    if req.status_code in invalid_status_code:
        print('Invalid Request and status code : ', req.status_code)
        print(req.content)
    else:
        req_json_data = json.loads(str(json_data))
        print(req.content)
        title = req_json_data["title"]
        print("Title - ", title)
        
for test_post_content in post_body_content:
    print(test_post_content)
    post_validation(test_post_content)



