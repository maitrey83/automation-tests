import requests

readfile = open('latte-1210-buying-guides.txt', 'r')
linebyline = readfile.readlines()
invalidurlcount = 0
for line in linebyline:
    verifyReq = requests.get(line.rstrip('\n')).status_code
    #print (str(line.rstrip('\n'))+ '- Status Code - '  + str(verifyReq))
    if verifyReq != 200:
        print("Image is 404 - " + str(line.rstrip('\n')))
        invalidurlcount = invalidurlcount + 1
print(invalidurlcount)
