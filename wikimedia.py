# Search English Wikipedia for up to 20 pages containing information about Jupiter
import requests


url = 'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={topic}&gsrnamespace=6&prop=imageinfo&iiprop=url&format=json'
headers = {
    'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'
}
params = {
    'q': 'jupiter',
    'limit': '20'
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

print(data)