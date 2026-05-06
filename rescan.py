from internetarchive import get_item, search_items
from bs4 import BeautifulSoup

cardCountTotal = 0
uploaderList = ['associate-axia-barish', 'associate-cameron-patera', 'associate-danielle-leard', 'associate-dylan-lewis', 'elijah_jarret', 'associate-emmie-zimmer', 'fernando_sibrian', 'associate-fredy-udave', 'associate-hope-snipes', 'associate-jay-luca', 'associate-josh-salazar', 'associate-kurt-hamilton', 'louis.brizuela@archive.org', 'associate-maeve-iwasaki', 'associate-maya-pearsall', 'associate-michael-arp', 'associate-miguel-salazar', 'associate-sophia-huang', 'associate-annie-russell', 'associate-vinny-taylor', 'associate-xaneath-nelson']
uploaderArgList = ['axia', 'cameron', 'danielle', 'dylan', 'elijah', 'emmie', 'fernando', 'fredy', 'hope', 'jay', 'josh', 'kurt', 'louis', 'maeve', 'maya', 'michael', 'miguel', 'sophia', 'sylvie', 'vinny', 'xane']
for indexUploader, a in enumerate(uploaderList):
    allItems = []
    for iSearch in search_items(f'uploader:{a} micro_review:rescan'):
        allItems.append(iSearch['identifier'])
    itemCountTotal = len(allItems)
    print(itemCountTotal)
    print(allItems)

    with open(f"/home/gark/MicroficheScanning/scanners/{uploaderArgList[indexUploader]}.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        soup.find(id=f"{uploaderArgList[indexUploader]}RescansTotal").string = str(itemCountTotal)
        soup.find(id=f"{uploaderArgList[indexUploader]}RescansID").clear()
        for indexItems, b in enumerate(allItems):
            newListTag = soup.new_tag("li")
            newAnchorTag = soup.new_tag("a", href=f"https://archive.org/details/{str(b)}")
            newAnchorTag.string = str(b)
            newListTag.append(newAnchorTag)
            soup.find(id=f"{uploaderArgList[indexUploader]}RescansID").insert(1, newListTag)
    with open(f"/home/gark/MicroficheScanning/scanners/{uploaderArgList[indexUploader]}.html", "w") as fp:
        fp.write(soup.prettify())
