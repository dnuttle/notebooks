import requests
url = "http://localhost:9200/_search"
data = requests.get(url).json()
print(data)
