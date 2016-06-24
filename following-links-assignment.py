import urllib.request as ur
from bs4 import BeautifulSoup
import re
mainurl = 'http://python-data.dr-chuck.net/known_by_Mayra.html'
count = range(7)
position = 18
name = None

for link in count:
    def getname(url):
        html = ur.urlopen(mainurl).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.findAll('a')
        name = re.findall('.href="(\S+)">', str(tags))
        name = name[position]
        print (name)
        return name
    
getname(mainurl)






#for counts in count:
#for tag in tags:
 #   name = re.findall('.href="(\S+)">', str(tags))
  #  print (name)





#for link in links:
 #   html = ur.urlopen(link).read()
  #  soup = BeautifulSoup(html, 'html.parser')
   # tags = soup.findAll('a')
    #name = re.findall('.href="(\S+)">', str(tags))
     #print (name[position])
        


###
#html = ur.urlopen(tag).read()
#soup = BeautifulSoup(html, 'html.parser')
#tags = soup.findAll('a')
#name = re.findall('.html">(\S+)</a', str(tags))
#print (name[position])

#for links in tag:
 #   url = links
  #  html = ur.urlopen(url).read()
   # soup = BeautifulSoup(html, 'html.parser')
    #tags = soup.findAll('a')
    #name = re.findall('.html">(\S+)</a', str(tags))
    #print (name[position])
