from internetarchive import get_item, search_items
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

cardCountTotal = 0
uploader = 'associate-dylan-lewis'
# print("Current selected uploader is: " + uploader)

currentDay = datetime.now()
currentDayComplete = currentDay.strftime("%Y%m%d") + "000000"
nextDay = currentDay + timedelta(days=1)
nextDayComplete = nextDay.strftime("%Y%m%d") + "000000"
# print(currentDayComplete, nextDayComplete)

allItems = set()
for i in search_items(f'uploader:{uploader} scandate:[{currentDayComplete} TO {nextDayComplete}]'):
    allItems.add(i['identifier'])
itemCountTotal = len(allItems)
# print(itemCountTotal)

for i in range(1, 20):
    items = set()
    for j in search_items(f'uploader:{uploader} cardcount:{i} scandate:[{currentDayComplete} TO {nextDayComplete}]'):
        items.add(j['identifier'])
        allItems.discard(j['identifier'])
    cardCountTotal += (len(items) * i)

# print("Currently at " + str(cardCountTotal))

if len(allItems) > 0:
    print("Found " + str(len(allItems)) + " additional items.")
    for i in allItems:
        bigItem = get_item(i)
        cardCountTotal += int(bigItem.metadata.get('cardcount'))
    else:
        print("No large items found")

# print("Card count so far: " + str(cardCountTotal))
# print("Item count so far: " + str(itemCountTotal))

with open("/home/gark/MicroficheScanning/scanners/dylan.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    soup.find(id="DylanToday").string = str(cardCountTotal)
with open("/home/gark/MicroficheScanning/scanners/dylan.html", "w") as fp:
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
