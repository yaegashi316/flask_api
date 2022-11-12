import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")

# print(res.text["status"])
json = res.json()
result01 = json["results"][0]
print(json()["results"][0]["address1"])
print(json()["results"][0]["address2"])
print(json()["results"][0]["address3"])
print(json()["results"][0]["prefcode"])
