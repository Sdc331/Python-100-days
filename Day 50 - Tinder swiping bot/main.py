import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

MAIL = 'projectacc1571@gmail.com'
APPPASS = os.environ.get('APPPASS')
URL = "https://www.tinder.com"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(URL)

time.sleep(1)
try:
    driver.find_element(By.CSS_SELECTOR, "#c1054502469 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > div > header > div > div.D\(f\).Ai\(c\).Fxs\(0\) > div:nth-child(2) > a > div.w1u9t036 > div.c9iqosj").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "#c-673878607 > div > div.Expand--s.theme-light > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div.H\(100\%\).D\(f\).Fxd\(c\) > div.Mt\(a\) > span > div:nth-child(2) > button > div.w1u9t036 > div.c9iqosj").click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    print("Successfully changed window")
    driver.find_element(By.CSS_SELECTOR, "body > div._10.uiLayer._4-hy._3qw > div > div > div > div > div > div:nth-child(3) > div.x1exxf4d.x13fuv20.x178xt8z.x1l90r2v.xv54qhq.xf7dkkf > div > div:nth-child(2) > div.x1i10hfl.xjbqb8w.x1ejq31n.x18oe1m7.x1sy0etr.xstzfhl.x972fbf.x10w94by.x1qhh985.x14e42zd.x1ypdohk.xe8uvvx.xdj266r.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x16tdsg8.x1hl2dhg.xggy1nq.x1fmog5m.xu25z0z.x140muxe.xo1y3bh.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3 > div").click()
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys(MAIL)
    driver.find_element(By.CSS_SELECTOR, "#pass").send_keys(APPPASS)
    driver.find_element(By.CSS_SELECTOR, "#loginbutton").click()
    time.sleep(8)
    # driver.find_element(By.CSS_SELECTOR, "#mount_0_0_Q5 > div > div > div > div > div > div > div.x9f619.x1ja2u2z.x78zum5.x1q0g3np.x1iyjqo2.x1t2pt76.x1n2onr6.xvrxa7q.x1nhjfyr > div.x9f619.x2lah0s.x1n2onr6.x78zum5.x1iyjqo2.x1t2pt76.x1lspesw > div > div > div > div > div > div > div > div > div:nth-child(3) > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xyamay9 > div > div > div > div:nth-child(1) > div > div > div > div > div").click()
    # driver.find_element(By.CSS_SELECTOR, "body > div > div > div > div > div > div > div > div.x9f619.x1ja2u2z.x78zum5.x1q0g3np.x1iyjqo2.x1t2pt76.x1n2onr6.xvrxa7q.x1nhjfyr > div.x9f619.x2lah0s.x1n2onr6.x78zum5.x1iyjqo2.x1t2pt76.x1lspesw > div > div > div > div > div > div > div > div > div:nth-child(3) > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xyamay9 > div > div > div > div:nth-child(1) > div > div > div > div > div")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]").click()
    # driver.switch_to.window(driver.window_handles[0])
except:
    pass