from bs4 import BeautifulSoup
import requests
import re

def relcanonical_https():
    #readFile = open('https_rel_canonical_find.txt', 'r')
    readFile = open('https_rel_canonical_find_static.txt', 'r')
    lines = readFile.readlines()
    numberofurls = 0
    for urls in lines:
        reqs = requests.get(urls.rstrip('\n'))
        soup = BeautifulSoup(reqs.content, 'html.parser')
        #desc = soup.find("meta", {"name": "description"})['content']
        #print (desc)
        try:
            relCans = soup.find("link", {"rel": "canonical"})
            relNext = soup.find("link", {"rel": "next"})
            #print(relCans)
            cans = re.findall('\"http://www.*\" ', str(relCans))
            #cansnext = re.findall('\"http://www.*\" ', str(relNext))
            if cans != []:
                print("Rel Canonical ", cans)
                #print('Rel Next' + cansnext)
                numberofurls = numberofurls + 1
            '''if cans is not None:
                print ('url with rel canonicals - ' + str(urls.rstrip('\n')))
                print ('Rel Canonicals - '+ str(cans))
                print ()'''

            #print(relCans)
        except (NameError, TypeError):
            pass
    print ('Number of urls with Rel Canonical http = ' + str(numberofurls))
relcanonical_https()