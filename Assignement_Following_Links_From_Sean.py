import urllib.request as ur
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
position = 17
name = None

nextUrl = 'http://python-data.dr-chuck.net/known_by_Mayra.html'
for i in range(7):
    html = ur.urlopen(nextUrl).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.findAll('a')
    name = re.findall('.href="(\S+)">', str(tags))
    nextUrl = name[position]
    print("going to " + nextUrl + " next.")
