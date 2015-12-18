import sys
import urllib
import requests
def ValidateURL():

    fo = open("/home/kgokhale/LATTE-1050/Find_Redirect/Result_True.txt","r+")
    for line in urllib.urlopen('/home/kgokhale/LATTE-1050/Find_Redirect/To_Validate.txt'):
        r = requests.get(line.strip("\r\n"), allow_redirects=True)
        r.status_code
        r.history
        r.url

        writeOriginalURL = "Original URL: " + str(line)
        writeStatusCode = "Status code: " + str(r.status_code) + "\n"
        writeHistory = "Redirected Status Code: " + str(r.history) + "\n"
        writeUrl = "Redirected URL: " + str(r.url) + "\n" + "\n"

        fo.write(writeOriginalURL)
        fo.write(writeStatusCode)
        fo.write(writeHistory)
        fo.write(writeUrl)
    fo.close()

def main():
    ValidateURL()
main()