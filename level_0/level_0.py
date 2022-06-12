#!/usr/bin/python3
import requests

url = "http://158.69.76.135/level0.php"
data = {
    "id": "4561",
    "holdthedoor": "Submit"
}

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(url, data)
