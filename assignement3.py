hrs = 45
rate = 10.50
h = float(hrs)
p = float(rate)
regularhours = 40
rhours = float(regularhours)
extrahours = h - rhours
extrapay = extrahours*p*1.5
regularpay = rhours*p
totalpay = extrapay + regularpay
print (totalpay)
