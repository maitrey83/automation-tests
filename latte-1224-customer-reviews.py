import requests
from bs4 import BeautifulSoup

readfile = open('latte-1224-reviews.txt', 'r')
linebyline = readfile.readlines()
invalidurlcount = 0
for line in linebyline:
    req = requests.get(line.rstrip('\n'), allow_redirects=False)
    verifyReq = requests.get(line.rstrip('\n'), allow_redirects=False).status_code
    soup = BeautifulSoup(req.content, 'html.parser')
    #print(req)
    #print (str(line.rstrip('\n'))+ '  - Status Code - '  + str(verifyReq))
    if verifyReq != 404:
        print("URL is - " + str(line.rstrip('\n')) + " Status Code - "+ str(verifyReq))
        print(soup.title)
        invalidurlcount = invalidurlcount + 1
    elif verifyReq == 500:
        print("This is very bad URL " + str(line.rstrip('\n')))
print(invalidurlcount)