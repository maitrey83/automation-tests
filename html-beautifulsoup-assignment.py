import urllib.request as ur
from bs4 import BeautifulSoup
import re
url = 'http://python-data.dr-chuck.net/comments_229360.html'
html = ur.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('td')
#print (tags)
score = re.findall('[0-9]+', str(tags))
score = [int(i) for i in score]
score = sum(score)
print (score)
