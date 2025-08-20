import json


import httpx


base_url = "http://localhost:8000"


def check_get_1():
    files_endpoint = "/files/abc.txt"

    url = base_url + files_endpoint
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


def check_post_1():

    final_endpoint = "/items/"

    url = base_url + final_endpoint

    payload: dict[str, str | int] = {
        "name": "Rana Universe Book",
        "price": 250,
        "description": "This is a good book written for our universe.",
        "tax": 20,
        "extra_key_1": 111,
        "extra_key_2": 222,
        "extra_key_3": 333,
    }

    params = {"tax": 15, "poo": 12}

    response = httpx.post(url, json=payload, params=params)

    status_code = response.status_code

    if status_code == 200:
        print("✅ POST request success (200 OK)")
        resp_dict = json.loads(response.text)
        print(resp_dict)
    else:
        print("❌ POST request failed")
        print("Status Code:", response.status_code)
        try:
            print(response.json())
        except Exception:
            print(response.text)


def check_get_2():
    final_endpoint = "/time/"
    url = base_url + final_endpoint
    parameters_dict = {"after_minute": 20}
    response = httpx.get(url=url, params=parameters_dict)
    print(response.json())


if __name__ == "__main__":
    # check_get_1()
    # check_post_1()
    check_get_2()
