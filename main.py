import json


import httpx


base_url = "http://localhost:8000"

files_endpoint = "/files/abc.txt"

url = base_url + files_endpoint
url = "http://localhost:8000/users/12/items/98"


def check_get_1():
    response = httpx.get(url)

    status_code = response.status_code

    if status_code == 200:
        print("Good Connection Established with 200")

        resp_dict = json.loads(response.text)
        print(resp_dict)

    else:
        print("Not Good Result")
        print("Status Code:", response.status_code)
        print(response.json())


if __name__ == "__main__":
    check_get_1()
