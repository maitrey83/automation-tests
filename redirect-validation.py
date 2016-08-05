import requests
redirects = open("redirects.txt","r+")
read_redirects = redirects.readlines()



for line in read_redirects:
    verifyredirects = requests.get(line.strip('\r\n'), allow_redirects=True)
    status = verifyredirects.status_code
    #print(status)
    if status != 200:
        print (line + ' ' +str(status))

