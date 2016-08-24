from bs4 import BeautifulSoup
import requests
import re
def siteWideRemovalsOfMetaKeywords():
    readFile = open('LATTE-1484-Add-No-Follow-No-Index.txt', 'r')
    lines = readFile.readlines()
    numberofurls = 0
    for urls in lines:
        reqs = requests.get(urls.rstrip('\n'))
        soup = BeautifulSoup(reqs.content, 'html.parser')
        #print ("Title - " + soup.title.string)
        metaContent = str(soup.find("meta", {"content": "noindex,nofollow"}))
        print(metaContent)
        #print("No Follows No Index - " +str(soup.find("meta", {"content": "noindex,nofollow"})))
        noFollows = re.search('.meta content=(\s+)>', str(metaContent))
        #print("Content Displayed - " + )
        print(noFollows)
        #print("Rel Canonicals - " +str(soup.find("link", {"rel": "canonical"})))
siteWideRemovalsOfMetaKeywords()