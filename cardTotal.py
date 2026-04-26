from internetarchive import get_item, search_items
import json
from datetime import datetime, timedelta

cardCountTotal = 0
uploader = 'associate-dylan-lewis'
print("Current selected uploader is: " + uploader)

allItems = set()
for i in search_items(f'uploader:{uploader}'):
    allItems.add(i['identifier'])
itemCountTotal = len(allItems)

for i in range(1, 25):
    items = set()
    for j in search_items(f'uploader:{uploader} cardcount:{i}'):
        items.add(j['identifier'])
        allItems.discard(j['identifier'])
    cardCountTotal += (len(items) * i)

print("Currently at " + str(cardCountTotal))

if len(allItems) > 0:
    print("Found " + str(len(allItems)) + " additional items.")
    for i in allItems:
        bigItem = get_item(i)
        cardCountTotal += int(bigItem.metadata.get('cardcount'))

print("Card count so far: " + str(cardCountTotal))
print("Item count so far: " + str(itemCountTotal))

# filename = "test_" + datetime.now().strftime("%H%M%S_%Y%m%d") + ".json"
# with open(filename, "w") as file:
#     data = {
#         "date": previousDayFormat,
#         "item_count": itemCountTotal,
#         "cardcount_total": cardCountTotal
#     }
#     json.dump(data, file, indent=2)
# print(f"Data exported to {filename}")
