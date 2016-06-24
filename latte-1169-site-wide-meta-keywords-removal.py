from bs4 import BeautifulSoup
import requests

def siteWideRemovalsOfMetaKeywords():
    readFile = open('latte-1169-meta-keywords-data-set.txt', 'r')
    lines = readFile.readlines()
    numberofurls = 0
    for urls in lines:
        reqs = requests.get(urls.rstrip('\n'))
        soup = BeautifulSoup(reqs.content, 'html.parser')
        #desc = soup.find("meta", {"name": "description"})['content']
        #print (desc)
        try:
            keywords = soup.find('meta', {'name':'keywords'})['content']
            if keywords is not None:
                print ('url with meta keywords - ' + str(urls.rstrip('\n')))
                print ('Keywords - '+ str(keywords))
                print ()
                numberofurls = numberofurls + 1
        except (NameError, TypeError):
            pass    
    print ('Number of urls with keywords = ' + str(numberofurls))
siteWideRemovalsOfMetaKeywords()
