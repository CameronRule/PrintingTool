import math

printingPrice = {
    "1" : "0.08", #A4 black and white
    "2" : "0.16" #A3 Black and White
}

finishingPrice = {
    '':'',
    '':''
}

pageSize = input("What size would you like this page to be [1]A4 or [2]A3")
while True: 
    printColour = input("Would you like the document in [B]lack and White or [C]olour")
    if printColour.upper() == "C":
        price = printingPrice[pageSize] * 8.5
print(price)



pageSide = input("Would you like this document to be [D]ouble Sided or [S]ingle sided")


