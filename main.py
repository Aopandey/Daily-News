import requests
from send_email import send_mail

category = "business"
key = "88a43250dd8f4f2d973cd15b274ebfa9"
url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=88a43250dd8f4f2d973cd15b274ebfa9"

req = requests.get(url)

data = req.json()

subject = "Today's News Headlines"
body = ""
for i in data["articles"][:20]:
    title = i["title"]
    description = i["description"]
    url = i["url"] or ""
    body += f"{title}\n{description}\n\n{url}\n\n"

send_mail(subject, body)

