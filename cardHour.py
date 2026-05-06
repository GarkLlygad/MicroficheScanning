from internetarchive import get_item, search_items
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

dayShiftStart = "130000"
dayShiftEnd = "125900"
nightShiftStart = "220000"
nightShiftEnd = "215900"

currentDay = datetime.now()
nextDay = currentDay + timedelta(days=1)

nightShiftList = ["michael", "jay", "hope", "axia", "danielle", "josh", "sylvie", "sophia", "maeve", "xane"]
if uploaderArg in nightShiftList:
    currentDayComplete = currentDay.strftime("%Y%m%d") + nightShiftStart
    nextDayComplete = nextDay.strftime("%Y%m%d") + nightShiftEnd
else:
    currentDayComplete = currentDay.strftime("%Y%m%d") + dayShiftStart
    nextDayComplete = nextDay.strftime("%Y%m%d") + dayShiftEnd

print(currentDayComplete, nextDayComplete)

allItems = set()
for i in search_items(f'uploader:{uploader} scandate:[{currentDayComplete} TO {nextDayComplete}]'):
    allItems.add(i['identifier'])
itemCountTotal = len(allItems)
print("Total item count: " + str(itemCountTotal))

if itemCountTotal > 0:
    for i in range(1, 20):
        items = set()
        for j in search_items(f'uploader:{uploader} cardcount:{i} scandate:[{currentDayComplete} TO {nextDayComplete}]'):
            items.add(j['identifier'])
            allItems.discard(j['identifier'])
        cardCountTotal += (len(items) * i)

    print("Currently at " + str(cardCountTotal) + " cards")

    if len(allItems) > 0:
        print("Found " + str(len(allItems)) + " additional items.")
        for i in allItems:
            bigItem = get_item(i)
            cardCountTotal += int(bigItem.metadata.get('cardcount'))
        else:
            print("No large items found")

    print("Card count so far: " + str(cardCountTotal))
    print("Item count so far: " + str(itemCountTotal))
else:
    print("No items found")


with open(f"/home/gark/MicroficheScanning/scanners/{uploaderArg}.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    soup.find(id=f"{uploaderArg}Today").string = str(cardCountTotal)
with open(f"/home/gark/MicroficheScanning/scanners/{uploaderArg}.html", "w") as fp:
    fp.write(soup.prettify())
