from bs4 import BeautifulSoup
import requests

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
class DataMiner():

    def __init__(self):
        data = requests.get(ZILLOW_URL)
        data.encoding = "utf-8"
        self.output = data.text
        self.soup = BeautifulSoup(self.output, 'html.parser')

    def get_data(self):
        self.objectList = self.soup.find("ul", class_="List-c11n-8-84-3-photo-cards")
        links = self.objectList.find_all("a", class_="StyledPropertyCardDataArea-anchor")
        addresses = self.objectList.find_all("address")
        data1 = [link.get("href") for link in links]
        data2 = [each.text.strip() for each in addresses]
        print(data1)