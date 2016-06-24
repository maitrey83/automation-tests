from bs4 import BeautifulSoup
import requests
def siteWideRemovalsOfMetaKeywords():
    readFile = open('content-hubs-automation-urls.txt', 'r')
    lines = readFile.readlines()
    numberofurls = 0
    for urls in lines:
        reqs = requests.get(urls.rstrip('\n'))
        soup = BeautifulSoup(reqs.content, 'html.parser')
        print ("Title - " + soup.title.string)
        print("Description - " + soup.find("meta", {"name": "description"})['content'])
        print("Rel Canonicals - " +str(soup.find("link", {"rel": "canonical"})))
siteWideRemovalsOfMetaKeywords()