import requests
import random
from bs4 import BeautifulSoup as bs

specifier = "<Enter Your Specifier here>"

url = "https://www.polltab.com/api/poll/"+specifier+"/vote"

proxies = []
def get_proxies():
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies


def get_session(proxies):
    session = requests.Session()
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session


if _name_ == "_main_":
    
    x = {
            <Paster your Data Here>
        }

    get_proxies()
    
    for i in range(len(proxies)):
        s = get_session(proxies)
        try:
            requests.post(url, proxies=proxies, data=x, allow_redirects=False)
            print('vote ah potaachu')
        except Exception as e:
            continue