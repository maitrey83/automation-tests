import openpyxl
import os
import requests
from bs4 import BeautifulSoup

# 1.0 Read urls from the excel file
# 1.1 Change the current path of the file
path = "C:\\Users\\maitreypatel\\Desktop\\TaxonomyUpdates\\LATTE-931-Pets-Taxonomy"
workBook = "Pets_Taxonomy_Update_V1.3.xlsx"
sheetNameRename = "Taxonomy Changes"
sheetNameInsert = "Insert Validation"
sheetNameDelete = "Delete Validation"
sheetNameRedirect = "Redirect Validation"
mainurl = 'https://www.overstock.com/'
forwardslash = '/'
html = '.html'


def changeDirectory():
    changedir = os.chdir(path)
def verifyinserts(level, id):
    buildurl = str(mainurl) + str(taxonomyid) +str(forwardslash) + str(taxonomylevel) + str(html)
    #print (buildurl)
    req_status = requests.get(buildurl).status_code
    #print (req_status)
    if req_status != 200:
        print ('url Status is ' + str(req_status))
        print (buildurl)
        #print (req_status)
def verifyrenames(level, id):
    buildurl = str(mainurl) + str(taxonomyid) +str(forwardslash) + str(taxonomylevel) + str(html)
    #print (buildurl)
    req = requests.get(buildurl)
    try:
        soup = BeautifulSoup(req.content, 'html.parser')
        crumbList=soup.find("div", {"id": "brd-crumbs"}).find_all("span")[0].text
        if crumbList != desirednames:
            print ('Shopping Site Name - ' + crumbList + ' Desired Excel Name - ' + desirednames + '  ' +'rename is not matching')
            print (buildurl)
    except(AttributeError, TypeError):
        print(str(taxonomyid) + '  ' + str(taxonomylevel) + ' ' + 'no values found')

def verifydeletes(level, id):
    buildurl = str(mainurl) + str(deletedtaxid) +str(forwardslash) + str(deletedtaxlevel) + str(html)
    print (buildurl)
def verifyredirects(level, id):
    buildurl = str(mainurl) + str(deletedtaxid) +str(forwardslash) + str(deletedtaxlevel) + str(html)
    reqredirects = requests.get(buildurl, allow_redirects=True)
    try:
        soup = BeautifulSoup(reqredirects.content, 'html.parser')
        redirectname = soup.find("div", {"id": "brd-crumbs"}).find_all("span")[0].text
        print('original url -' + buildurl)
        print(str(reqredirects.history) + ' redirect name ' + redirectname+' Redirected Url - ' + str(reqredirects.url))
    except (AttributeError, TypeError):
        print (str(deletedtaxid) + '   ' + str(deletedtaxlevel) + ' No products found ' )

getType = openpyxl.load_workbook(workBook).get_sheet_by_name(sheetNameRename)
for row in range(2, getType.get_highest_row() + 1):
    type = getType['A' + str(row)].value
    taxonomylevel = getType['C' + str(row)].value
    taxonomyid = getType['E' + str(row)].value
    deletedtaxlevel = getType['B' + str(row)].value
    deletedtaxid = getType['D' + str(row)].value
    desirednames = getType['H' + str(row)].value
    if type == 'added':
        verifyinserts(taxonomylevel, taxonomyid)
        #print (str(type) + '  ' + str(taxonomylevel) +  '  '  + str(taxonomyid))
    elif type == 'renamed':
        verifyrenames(taxonomylevel, taxonomyid)
        #print (str(type) + '  ' + str(taxonomylevel) +  '  '  + str(taxonomyid))
    elif type == 'deleted':
        verifyredirects(deletedtaxlevel, deletedtaxid)
        #print (str(type) + '  ' + str(deletedtaxlevel) +  '  '  + str(deletedtaxid))
    else:
        print ('not recognized type')

    #print (str(type) + '  ' + str(taxonomylevel) +  '  '  + str(taxonomyid))
    #buildurl = str(mainurl) + str(taxonomyid) +str(forwardslash) + str(taxonomylevel) + str(html)
    #print (buildurl)
