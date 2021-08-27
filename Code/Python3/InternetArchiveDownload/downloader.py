from internetarchive import download
from internetarchive import configure

login = open("ia_login.txt", "r")
configure(login.readline().strip(), login.readline().strip())

identifier = input("What is the Identifier of the archive? ").strip()

download(identifier, formats=["Cue Sheet", "Flac"], verbose=True, destdir="downloads", retries=2, ignore_errors=True, ignore_existing=True)
