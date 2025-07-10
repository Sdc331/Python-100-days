import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

MAIL = 'projectacc1571@gmail.com'
MAILPASS = os.environ.get('LINKPASS')
APPPASS = os.environ.get('APPPASS')
URL =  'https://www.linkedin.com/jobs/search/?currentJobId=4261893523&f_AL=true&f_WT=2&keywords=Python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(URL)
time.sleep(3)
try:
    # driver.find_element(By.CSS_SELECTOR, ".contextual-sign-in-modal__btn-container .sign-in-modal__outlet-btn").click()
    driver.find_element(By.CSS_SELECTOR, '#base-contextual-sign-in-modal > div > section > button > icon > svg').click()
    driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-secondary-emphasis.btn-md").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(MAIL)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(APPPASS)
    driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button').click()
except:
    pass
# driver.quit()