from bs4 import BeautifulSoup

uploaders = ['dylan', 'elijah', 'fernando', 'axia', 'cameron', 'danielle', 'emmie', 'fredy', 'hope', 'jay', 'josh', 'kurt', 'maeve', 'maya', 'michael', 'wesley', 'sophia', 'sylvie', 'vinny', 'xane']

for uploaderArg in uploaders:
    with open(f"/home/gark/MicroficheScanning/scanners/{uploaderArg}.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        soup.find(id=f"{uploaderArg}Today").string = str(0)
    with open(f"/home/gark/MicroficheScanning/scanners/{uploaderArg}.html", "w") as fp:
        fp.write(soup.prettify())
