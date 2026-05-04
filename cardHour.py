from internetarchive import get_item, search_items
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import sys

cardCountTotal = 0
uploaderArg = sys.argv[1]
uploaderlist = ['associate-dylan-lewis', 'elijah_jarret', 'fernando_sibrian', 'associate-axia-barish', 'associate-cameron-patera', 'associate-danielle-leard', 'associate-emmie-zimmer', 'associate-fredy-udave', 'associate-hope-snipes', 'associate-jay-luca', 'associate-josh-salazar', 'associate-kurt-hamilton', 'associate-maeve-iwasaki', 'associate-maya-pearsall', 'associate-michael-arp', 'associate-miguel-salazar', 'associate-sophia-huang', 'associate-annie-russell', 'associate-vinny-taylor', 'associate-xaneath-nelson', 'louis.brizuela@archive.org']
if uploaderArg == "sylvie":
    uploader = 'associate-annie-russell'
else:
    for i in uploaderList:
        if uploaderArg in i:
            uploader = i
            print("Found", str(uploader), "in", str(i))
print("Current selected uploader is: " + uploader)

currentDay = datetime.now()
currentDayComplete = currentDay.strftime("%Y%m%d") + "000000"
nextDay = currentDay + timedelta(days=1)
nextDayComplete = nextDay.strftime("%Y%m%d") + "000000"
print(currentDayComplete, nextDayComplete)

allItems = set()
for i in search_items(f'uploader:{uploader} scandate:[{currentDayComplete} TO {nextDayComplete}]'):
    allItems.add(i['identifier'])
itemCountTotal = len(allItems)
print(itemCountTotal)

if itemCountTotal > 0:
    for i in range(1, 20):
        items = set()
        for j in search_items(f'uploader:{uploader} cardcount:{i} scandate:[{currentDayComplete} TO {nextDayComplete}]'):
            items.add(j['identifier'])
            allItems.discard(j['identifier'])
        cardCountTotal += (len(items) * i)

    print("Currently at " + str(cardCountTotal))

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


with open(f"scanners/{uploaderArg}.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    soup.find(id=f"{uploaderArg}Today").string = str(cardCountTotal)
with open(f"scanners/{uploaderArg}.html", "w") as fp:
    fp.write(soup.prettify())

# filename = "test_" + datetime.now().strftime("%H%M%S_%Y%m%d") + ".json"
# with open(filename, "w") as file:
#     data = {
#         "date": previousDayFormat,
#         "item_count": itemCountTotal,
#         "cardcount_total": cardCountTotal
#     }
#     json.dump(data, file, indent=2)
# print(f"Data exported to {filename}")
