import requests

readfile = open('static-page-urls-6.txt', 'r')
linebyline = readfile.readlines()
count = 0
redirectcount = 0
validurlcount = 0
ohno = "http://www.overstock.com/oh_no_shopping.html"
for line in linebyline:
    verifyReq = requests.get(line.strip('\r\n'), allow_redirects=True)
    status = verifyReq.status_code
    redirectedurl = verifyReq.url
    history = verifyReq.history[0].status_code
    #print (str(redirectedurl)+ '- Status Code - ' + str(history))
    if redirectedurl == ohno:
        pass
    elif history == 301:
        redirectcount = redirectcount + 1
    elif status == 404:
        print("Status code : " + str(status) + " Url : " + str(line))
        count = count + 1

print("200 urls count: " + str(count) + " Redirected url count: " + str(redirectcount))