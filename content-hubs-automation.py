from bs4 import BeautifulSoup
import requests
import re
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

def productListings():
    guideUrl = 'https://www.overstock.com/guides/handheld-gps-functions-and-features'
    guideReq = requests.get(guideUrl)
    soupGudie = BeautifulSoup(guideReq.content, 'html.parser')
    guides = str(soupGudie.find_all("div",{"class":"productListings"}))
    #productUrls = str(re.findall('\"https://www.*\"', guides))
    productUrls = str(re.findall('(https://www.+product.html)', guides))


    print('Product Links - ' + productUrls)

siteWideRemovalsOfMetaKeywords()
productListings()