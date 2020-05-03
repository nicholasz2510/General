import requests
from bs4 import BeautifulSoup as bs

f = open("config.txt", "r")
config_info = f.readlines()
f.close()


def get_links(login_url, site_url):
    with requests.Session() as s:
        login_data = {"email": config_info[0], "password": config_info[1]}
        s.post(login_url, login_data)
        home_page = s.get(site_url)

        soup = bs(home_page.text, 'html.parser')
        links = ["https://ica.wildapricot.org" + x["href"] for x in soup.find_all("a") if
                 x["href"].startswith("/r") and x["href"].endswith("f")]
        return links


all_links = []
pages = [str(x) for x in [18054, *range(18057, 18061), *range(18062, 18066)]]
for p in pages:
    all_links += get_links("https://ica.wildapricot.org/Sys/Login?ReturnUrl=%2fpage-" + p,
                           "https://ica.wildapricot.org/page-" + p)
print(all_links)

for url in all_links:
    r = requests.get(url, allow_redirects=True)
    open("pdfs/" + url.rsplit("/", 1)[1], "wb").write(r.content)
