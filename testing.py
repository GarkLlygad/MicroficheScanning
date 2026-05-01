from bs4 import BeautifulSoup

with open("scanners/dylan.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    soup.find(id="DylanTotal").string = "432"
with open("scanners/dylan.html", "w") as fp:
    fp.write(soup.prettify())