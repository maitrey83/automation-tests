import openpyxl
import os
import requests
from bs4 import BeautifulSoup
import re

path = "C:\\Users\\maitreypatel\\Desktop\\SEO\\TaxonomyUpdates"
workBook = "AGTaxonomy11.xlsx"
sheetNameRename = "Taxonomy Changes"
sheetNameRedirect = "Redirect for Deleted"
sheetNameInsert = "Insert Validation"
sheetNameDelete = "Delete Validation"
mainurl = 'https://www.overstock.com/'
forwardslash = '/'
html = '.html'
getType = openpyxl.load_workbook(workBook).get_sheet_by_name(sheetNameRename)
getSheetRedirect = openpyxl.load_workbook(workBook).get_sheet_by_name(sheetNameRedirect)

def changeDirectory():
    changedir = os.chdir(path)
def verifyinserts(level, id):
    buildurl = str(mainurl) + str(taxonomyid) +str(forwardslash) + str(taxonomylevel) + str(html)
    #print (buildurl)
    req_status = requests.get(buildurl).status_code
    print (req_status)
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
    buildurl = str(mainurl) + str(existingid) +str(forwardslash) + str(existinglevel) + str(html)
    reqredirects = requests.get(buildurl, allow_redirects=True)
    try:
        soup = BeautifulSoup(reqredirects.content, 'html.parser')
        redirectname = soup.find("div", {"id": "brd-crumbs"}).find_all("span")[0].text
        #print('original url -' + buildurl)
        #print(str(reqredirects.history))
        #print('redirect name ' + redirectname)
        redirectedUrl = str(reqredirects.url)
        print('Redirected Url - ' + str(redirectedUrl))
        originalredirecturl = str(mainurl) + str(originalredirectid) + str(forwardslash) + str(originalredirectlevel) + str(html)
        #print(originalredirecturl)
        redirected_id = re.search('./([0-9]+)', str(redirectedUrl))
        print(int(float(redirected_id.group(1))))
        if int(float(redirected_id.group(1))) != originalredirectid:
            print("error")
            print(redirected_id.group(1))
            print(originalredirectid)
            print(originalredirectname)
            print('redirect name ' + redirectname)
            print(originalredirecturl)
    except (AttributeError, TypeError):
        print (str(existingid) + '   ' + str(existinglevel) + ' No products found ' )


for row in range(2, getType.get_highest_row() + 1):
    type = getType['A' + str(row)].value
    taxonomylevel = getType['C' + str(row)].value
    taxonomyid = getType['E' + str(row)].value
    deletedtaxlevel = getType['B' + str(row)].value
    deletedtaxid = getType['D' + str(row)].value
    desirednames = getType['H' + str(row)].value

    if type == 'added':
        print (str(type) + '  ' + str(taxonomylevel) +  '  '  + str(taxonomyid))
        verifyinserts(taxonomylevel, taxonomyid)
    elif type == 'renamed':
        print (str(type) + '  ' + str(taxonomylevel) +  '  '  + str(taxonomyid))
        verifyrenames(taxonomylevel, taxonomyid)
    elif type == 'deleted':
        pass
    else:
        print ('not recognized type')

for row in range(2, getSheetRedirect.get_highest_row() + 1):
    existingid = getSheetRedirect['B' + str(row)].value
    existinglevel = getSheetRedirect['A' + str(row)].value
    originalredirectid = getSheetRedirect['E' + str(row)].value
    originalredirectlevel = getSheetRedirect['D' + str(row)].value
    originalredirectname = getSheetRedirect['F' + str(row)].value
    redirectTaxonomytype= getSheetRedirect['H' + str(row)].value

    print (str(existinglevel) +  '  '  + str(existingid))
    verifyredirects(existinglevel, existingid)







    #print (str(type) + '  ' + str(taxonomylevel) +  '  '  + str(taxonomyid))
    #buildurl = str(mainurl) + str(taxonomyid) +str(forwardslash) + str(taxonomylevel) + str(html)
    #print (buildurl)