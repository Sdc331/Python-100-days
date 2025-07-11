import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

OTHER_USER_URL = "https://www.instagram.com/cristiano/"
URL = "https://www.instagram.com"
USERNAME = os.environ.get("IGUSER")
PASSWORD = os.environ.get("IGPASS")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get(URL)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]").click()
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#loginForm > div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(5) > button > div > span").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "body > div._10.uiLayer._4-hy._3qw > div > div > div > div > div > div:nth-child(3) > div.x1exxf4d.x13fuv20.x178xt8z.x1l90r2v.xv54qhq.xf7dkkf > div > div:nth-child(2) > div.x1i10hfl.xjbqb8w.x1ejq31n.x18oe1m7.x1sy0etr.xstzfhl.x972fbf.x10w94by.x1qhh985.x14e42zd.x1ypdohk.xe8uvvx.xdj266r.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x16tdsg8.x1hl2dhg.xggy1nq.x1fmog5m.xu25z0z.x140muxe.xo1y3bh.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3 > div > div.html-div.xdj266r.xat24cr.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x6s0dn4.x78zum5.xl56j7k.x14ayic.xwyz465.x1e0frkt > div > span > span").click()
time.sleep(1)
driver.find_element(By.NAME, "email").send_keys(USERNAME)
driver.find_element(By.NAME, "pass").send_keys(PASSWORD)
driver.find_element(By.ID, "loginbutton").click()
time.sleep(15)
driver.get(OTHER_USER_URL)
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span/span').click()
time.sleep(5)
accounts = driver.find_elements(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.x1bphaa0.x18nydb4.xcm95gh.x1vsb9q8.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.x6nl9eh.x1a5l9x9.x7vuprf.x1mg3h75.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div > button")
# print(f"Accounts: {accounts}")
for each in range(10):
    accounts[each].click()
# for each in accounts:
#     each.click()

# driver.quit()
