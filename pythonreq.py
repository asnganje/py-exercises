import requests
url = "http://www.google.com/ljnfblk/dllfd"
res = requests.get(url)
print(f"Your request to {url} came back with response status {res.status_code}")