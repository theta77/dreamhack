import requests

url = "23.81.42.210"
res = requests.get(f"http://host3.dreamhack.games:21960/")
print(res.text)
