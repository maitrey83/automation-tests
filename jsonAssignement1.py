import urllib.request as ur
import json
import codecs
import re

url = 'http://python-data.dr-chuck.net/comments_229361.json'
print (url)
urlopen = ur.urlopen(url)
data = urlopen.read()
#print(data)
str_data = data.decode('utf-8')
info = json.loads(str_data)
print(str_data)
counts = re.findall( '.count":([0-9]+)', str_data)
print('total counts : ', len(counts))
totalvalues = []
for i in counts:
    values = i
    totalvalues.append(values)
#print(totalvalues)
totalvalues = [int(x) for x in totalvalues]
totalvalues = sum(totalvalues)
print(totalvalues)

