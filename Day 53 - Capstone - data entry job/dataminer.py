from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests, re, time

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf4GKAB7qXgjzDk0nIyvFz9EvEfrGLYMjROKOgx-YvN0xULew/viewform?usp=header"
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
        prices = self.objectList.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
        data1 = [link.get("href") for link in links]
        data2 = [each.text.strip() for each in addresses]
        # regex to remove string starting with "+" till end of line.
        data3 = [re.sub(r'\+.*', '', price.text).rstrip("/mo") for price in prices]
        self.apartment_data = [{"address": addr, "link": lnk, "price": prc}
                               for addr, lnk, prc in zip(data2, data1, data3)]
        
    def send_data(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        print(f"Length:{len(self.apartment_data)}")
        for each in self.apartment_data:
            self.driver.get(FORM_URL)
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(each['address'])
            self.driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(each['price'])
            self.driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(each['link'])
            self.driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span").click()
            time.sleep(1)
        self.driver.quit()
        print("All data transferred")