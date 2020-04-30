import requests
from bs4 import BeautifulSoup
from queue import Queue
import io

f = open("crawler_sites.txt", "w")
f.close()

q = Queue(maxsize=0)
discovered = {"https://www.wikipedia.org/"}
q.put("https://www.wikipedia.org/")
while not q.empty():
    v = q.get()
    soup = BeautifulSoup(requests.get(v).text, "html.parser")
    for a in soup.find_all("a"):
        link = str(a.get("href"))
        if link.startswith("//"):
            link = "https:" + link
        elif link.startswith("/"):
            link = "https://en.wikipedia.org" + link
        else:
            continue
        if link not in discovered:
            q.put(link)
            discovered.add(link)

            f = io.open("crawler_sites.txt", "a", encoding="utf-8")
            f.write(link + "\n")
            f.close()
