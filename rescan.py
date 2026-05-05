from internetarchive import get_item, search_items
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import sys

cardCountTotal = 0
uploaderArg = sys.argv[1]
uploaderList = ['associate-dylan-lewis', 'elijah_jarret', 'fernando_sibrian', 'associate-axia-barish', 'associate-cameron-patera', 'associate-danielle-leard', 'associate-emmie-zimmer', 'associate-fredy-udave', 'associate-hope-snipes', 'associate-jay-luca', 'associate-josh-salazar', 'associate-kurt-hamilton', 'associate-maeve-iwasaki', 'associate-maya-pearsall', 'associate-michael-arp', 'associate-miguel-salazar', 'associate-sophia-huang', 'associate-annie-russell', 'associate-vinny-taylor', 'associate-xaneath-nelson', 'louis.brizuela@archive.org']
if uploaderArg == "sylvie":
    uploader = 'associate-annie-russell'
else:
    for i in uploaderList:
        if uploaderArg in i:
            uploader = i
            print("Found", str(uploader), "in", str(i))
print("Current selected uploader is: " + uploader)

allItems = []
for i in search_items(f'uploader:{uploader} micro_review:rescan'):
    allItems.append(i['identifier'])
itemCountTotal = len(allItems)
print(itemCountTotal)
print(allItems)

with open(f"/home/gark/MicroficheScanning/scanners/{uploaderArg}.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    soup.find(id=f"{uploaderArg}RescansTotal").string = str(itemCountTotal)
    soup.find(id=f"{uploaderArg}RescansID").clear()
    for i,x in enumerate(allItems):
        newListTag = soup.new_tag("li")
        newAnchorTag = soup.new_tag("a", href=f"https://archive.org/details/{str(x)}")
        newAnchorTag.string = str(x)
        newListTag.append(newAnchorTag)
        soup.find(id=f"{uploaderArg}RescansID").insert(1, newListTag)
with open(f"/home/gark/MicroficheScanning/scanners/{uploaderArg}.html", "w") as fp:
    fp.write(soup.prettify())
