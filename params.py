import requests
url = "https://icanhazdadjoke.com/search"
term = input("Please enter your search term: \n")
res = requests.get(
    url, headers={"Accept": "application/json"},
    params={"term": f"{term}",
            "limit": 1})
data = res.json()
print(data)
