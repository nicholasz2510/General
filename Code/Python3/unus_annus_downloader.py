from internetarchive import download
from internetarchive import configure

login = open("ia_login.txt", "r")

configure(login.readline().strip(), login.readline().strip())
download('full-unus-annus-archive-2', verbose=True, destdir="C:/Users/nicho/Videos/UNUS ANNUS", ignore_errors=True, ignore_existing=True)
