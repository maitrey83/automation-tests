from bs4 import BeautifulSoup
import requests
import re

def siteWideRemovalsOfMetaKeywords():
    readFile = open('verify-ak1-s.txt', 'r')
    lines = readFile.readlines()

    numberofurls = 0
    for urls in lines:
        reqs = requests.get(urls.rstrip('\n'))
        soup = BeautifulSoup(reqs.content, 'html.parser')
        #print(soup)
        try:
            image = soup.find_all(string=re.compile("ak1-s"))
            #image = soup.find_all(string=re.compile('http'))
            #print(urls)
            if image != []:
                data = re.findall('(.http?[^\'"=,; >]+)', str(image))
                print(urls)
                print(data)
                #print(image)
        except(ConnectionError, TypeError, NameError):
            print(urls)
            pass
        #image = soup.find_all(string=re.compile("background: ([ak1]+)"))
        #print(image)
        #print(urls)

siteWideRemovalsOfMetaKeywords()