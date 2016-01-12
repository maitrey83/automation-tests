import requests

readfile = open('latte-1079.txt', 'r')
linebyline = readfile.readlines()
count = 0
for line in linebyline:
    verifyReq = requests.get(line.rstrip('\n')).status_code
    print (str(line.rstrip('\n'))+ '- Status Code - '  + str(verifyReq))
    if verifyReq != 200:
        print("Image is 404 -" + str(line))
        count = count + 1

