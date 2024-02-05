import requests

key = "88a43250dd8f4f2d973cd15b274ebfa9"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=88a43250dd8f4f2d973cd15b274ebfa9"

req = requests.get(url)
data = req.json()
for i in data["articles"]:
    print(i["title"])
    print(i["description"])
