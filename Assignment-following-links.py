import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

import os
import sys
module_path = os.path.abspath('..')
sys.path.append(os.path.abspath('..') + "/python/util/")
import scrape_util

nextUrl = 'http://python-data.dr-chuck.net/known_by_Mayra.html'
for i in range(7):
    bsObj = scrape_util.getBsObj(nextUrl)
    bsObjUl = bsObj.ul
    bsObjLi = bsObjUl.findAll("li")[17]
    nextUrl = bsObjLi.a.attrs['href']
    print("going to " + nextUrl + " next.")
