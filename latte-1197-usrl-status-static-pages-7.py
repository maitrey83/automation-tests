import requests
import sys
print(sys.argv)
readfile = open(sys.argv[1], 'r')
linebyline = readfile.readlines()
count = 0
redirectcount = 0
validurlcount = 0
for line in linebyline:
    verifyReq = requests.get(line.strip('\r\n'), allow_redirects=True)
    status = verifyReq.status_code
    redirectedurl = verifyReq.url
    history = verifyReq.history[0]
    #print (str(redirectedurl)+ '- Status Code - ' + str(history))
    if history == 200:
        print ("Invalid url " + str(line))

    if status != 200 and redirectedurl != "http://www.overstock.com":
        print("Status code : " + str(status) + " Url : " + str(line))
        count = count + 1

    elif status == 404:
        pass
print("200 urls " + str(count))