import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2025-05-24&to=2025-05-25&sortBy=popularity&language=en&apiKey=9853b28511e54cea831560910c357182')
content = r.json()

print(content['articles'])