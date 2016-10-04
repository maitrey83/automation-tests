from bs4 import BeautifulSoup
import requests
import re

def relcanonical_https():
    #readFile = open('https_rel_canonical_find.txt', 'r')
    readFile = open('https_rel_canonical_find_static.txt', 'r')
    #readFile = open('https_rel_canonical_find_static_weird_links', 'r')

    lines = readFile.readlines()
    numberofurls = 0
    for urls in lines:
        reqs = requests.get(urls.rstrip('\n'))
        soup = BeautifulSoup(reqs.content, 'html.parser')
        #desc = soup.find("meta", {"name": "description"})['content']
        #print (desc)
        try:
            #relCans = soup.find("link", {"rel": "canonical"})
            canonical = soup.find("link", rel = "canonical")
            #print(canonical)
            if canonical:
                canonical_url = canonical['href']
            else:
                print('No rel canonical present for the url ' + urls )
            #relNext = soup.find("link", {"rel": "next"})
            #print(relCans)
            cans = re.findall('(http://www.*)', str(canonical_url))
            #cansnext = re.findall('\"http://www.*\" ', str(relNext))
            if cans != []:
                print("Rel Canonical ", cans)
                print('URL- ' + urls)
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