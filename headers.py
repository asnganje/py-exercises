import requests
url = "https://icanhazdadjoke.com/#google_vignette"
res = requests.get(url, headers={
  "Accept":"application/json"
})

print(res.text)
print(res.json())