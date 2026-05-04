import sys
uploaderArg = sys.argv[1]
uploaderList = ['associate-dylan-lewis', 'elijah_jarret', 'fernando_sibrian', 'associate-axia-barish', 'associate-cameron-patera', 'associate-danielle-leard', 'associate-emmie-zimmer', 'associate-fredy-udave', 'associate-hope-snipes', 'associate-jay-luca', 'associate-josh-salazar', 'associate-kurt-hamilton', 'associate-maeve-iwasaki', 'associate-maya-pearsall', 'associate-michael-arp', 'associate-miguel-salazar', 'associate-sophia-huang', 'associate-annie-russell', 'associate-vinny-taylor', 'associate-xaneath-nelson', 'louis.brizuela@archive.org']
if uploaderArg == "sylvie":
    uploader = 'associate-annie-russell'
    print("Forcing associate-annie-russell")
else:
    for i in uploaderList:
        if uploaderArg in i:
            uploader = i
            print("Found", str(uploader), "in", str(i))


from bs4 import BeautifulSoup
with open(f"scanners/{uploaderArg}.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    soup.find(id=f"{uploaderArg}Today").string = "2000000000"
with open(f"scanners/{uploaderArg}.html", "w") as fp:
    fp.write(soup.prettify())


# from internetarchive import get_item, search_items
# allItems = set()
# for i in search_items('uploader:louis.brizuela@archive.org'):
#     allItems.add(i['identifier'])
# itemCountTotal = len(allItems)
# print(itemCountTotal)