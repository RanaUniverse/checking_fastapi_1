import json
import httpx

base_url = "http://localhost:8000"

files_endpoint = "/files/abc.txt"

url = base_url + files_endpoint

response = httpx.get(url)
resp = json.loads(response.text)
print(resp)


print(response.text)