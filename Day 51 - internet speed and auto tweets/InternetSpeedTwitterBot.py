import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

MAIL = "projectacc1571@gmail.com"
X_USER = "SpeedIsp70311"
XPASS = os.environ.get("XPASS")
SPEED_URL = "https://www.speedtest.net"
X_URL = "https://x.com/i/flow/login"

class SpeedBot:
    
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.down = 1000
        self.up = 100
        self.driver.maximize_window()
    
    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        time.sleep(2)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.driver.find_element(By.CSS_SELECTOR, "#container > div.pre-fold > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.start-button > a > span.start-text").click()
        time.sleep(45)
        self.driver.find_element(By.CSS_SELECTOR, "#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.main-view > div > div.desktop-app-prompt-modal > div > a > svg").click()
        self.actual_down = float(self.driver.find_element(By.CSS_SELECTOR, "#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span").text)
        self.actual_up = float(self.driver.find_element(By.CSS_SELECTOR, "#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span").text)
        print(f"{self.actual_down}, {self.actual_up}")


    def tweet_at_provider(self):
        if self.down > self.actual_down or self.up > self.actual_up:
            self.driver.get(X_URL)
            self.message = f"Reported speed:\n{self.actual_down}/{self.actual_up} Mbps\nExpected speed:\n{self.down}/{self.up} Mbps"
            try:
                time.sleep(2)
                self.driver.find_element(By.NAME, "text").send_keys(MAIL)
                self.driver.find_element(By.CSS_SELECTOR, "#layers > div > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-14lw9ot.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div > div > button:nth-child(6) > div").click()
                time.sleep(1)
                # To bypass X check due to suspicious login activity
                if self.driver.find_element(By.NAME, "text"):
                    self.driver.find_element(By.NAME, "text").send_keys(X_USER)
                    self.driver.find_element(By.CSS_SELECTOR, "#layers > div > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-14lw9ot.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-1f0wa7y > div > div > div > button").click()
                time.sleep(1)
                self.driver.find_element(By.NAME, "password").send_keys(XPASS)
                self.driver.find_element(By.CSS_SELECTOR, "#layers > div > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-14lw9ot.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-1f0wa7y > div > div.css-175oi2r > div > div > button > div").click()
            except:
                print("Login into X failed.")
            else:
                time.sleep(5)
                self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-14lw9ot.r-jxzhtn.r-1ua6aaf.r-th6na.r-1phboty.r-16y2uox.r-184en5c.r-1abdc3e.r-1lg4w6u.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div.css-175oi2r.r-14lw9ot.r-184en5c > div > div.css-175oi2r.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div").send_keys(self.message)
                self.driver.quit()
        else:
            print("Internet speed up to standard")