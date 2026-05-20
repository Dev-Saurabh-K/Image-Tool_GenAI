import requests

url = "https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=banana&gsrnamespace=6&prop=imageinfo&iiprop=url&format=json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(
        url=url,
        headers=headers,
        timeout=10
    )

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)