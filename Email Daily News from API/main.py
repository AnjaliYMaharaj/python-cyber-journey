'''
What is this project?
This app accesses news about a particular topic and sends them by email.
'''

import requests
from send_email import send_email

topic = "tesla"

api_key = "9853b28511e54cea831560910c357182"
url = (
    "https://newsapi.org/v2/everything?"
    f"q{topic}&"
    "q=tesla&"
    "sortBy=publishedAt&"
    "language=en&"
    f"apiKey={api_key}"
)

# Make request
request =  requests.get(url)

# Get a dictionary with data
content =  request.json()

#Access the articles titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
        + "\n" + body + article["title"] + "\n" \
        + article["description"] \
        + "\n" + article ["url"]+ 2*"\n"

body = body.encode("utf-8")
send_email(message=body)