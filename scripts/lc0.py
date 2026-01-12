import os
import bs4
import requests
os.chdir("src/lc0")
os.system("./build.sh")
os.rename("build/release/lc0", "../../bin/lc0")
os.chdir("../../bin/")
for file in os.listdir(os.getcwd()):
    if file.endswith(".pb.gz"):
        os.remove(file)
soup = bs4.BeautifulSoup(requests.get("https://lczero.org/play/networks/bestnets/").content, 'html.parser')
links = soup.find_all('a')
weights = []
for link in links:
    if '.pb.gz' in link.get('href'):
        weights.append(link)
with open(str(weights[-1]).split('"')[1].split('"')[0].split("/")[-1], "wb") as network:
    network.write(requests.get(str(weights[-1]).split('"')[1].split('"')[0]).content)