import urllib.request as ur
import xml.etree.ElementTree as ET
import re

serviceurl = 'http://python-data.dr-chuck.net/comments_229357.xml'
print (serviceurl)
urlopen = ur.urlopen(serviceurl)
data = urlopen.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
#print (counts.text)
print('total counts: ', len(counts))
#counts = [int (i) for i in counts]
#counts = sum(counts)
totalvalues = []
for i in counts:
    values = i.text
    totalvalues.append(values)
#print (totalvalues)
totalvalues = [int(x) for x in totalvalues]
totalvalues = sum(totalvalues)
print(totalvalues)







    
    

