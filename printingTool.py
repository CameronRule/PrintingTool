import math

printingPrice = {
    "1" : 0.08, #A4 black and white
    "2" : 0.16  #A3 Black and White
}

staplePrice = {
    '5': 0.01, #one staple
    '6': 0.02  #two staples
}

pageAmount = int(input("How many pages would you like good sire: "))
pageSize = input("What size would you like this page to be [1]A4 or [2]A3: ")
printColour = input("Would you like the document in [B]lack and White or [C]olour: ")
pageSide = input("Would you like this document to be [D]ouble Sided or [S]ingle sided: ")
finalPrice = printingPrice[pageSize]
staples = input("Would you like to use staples [Y] or [N]: ")

if printColour.upper() == "C":
   finalPrice = finalPrice * 8.5

if pageSide.upper() == "D":
    finalPrice = finalPrice * 2

finalPrice = finalPrice * pageAmount

if staples.upper() == "Y":
    numStaples = input("Would you like to use one [5] or two [6] staples: ")
    if numStaples.upper() == "5":
        finalPrice = finalPrice + (0.01 * pageAmount)
    else:
        finalPrice = finalPrice + (0.02 * pageAmount)


print("The final price of this order is" , round(finalPrice , 4))






