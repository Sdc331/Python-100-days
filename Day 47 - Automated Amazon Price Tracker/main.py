import requests, smtplib, os
from bs4 import BeautifulSoup

MINIMAL = 100
ADDR = os.environ.get("ADDR")
PASS = os.environ.get("ADDR_PASS")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0',
           'Accept-Language':'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'}

data = requests.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers=headers).text

soup = BeautifulSoup(data, "html.parser")
price_whole = float(soup.select_one(".a-price-whole").getText())
price_decimal = float(f"0.{soup.select_one('.a-price-fraction').getText()}")
price = price_whole + price_decimal

if price < MINIMAL:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(ADDR, PASS)
        connection.sendmail(msg=f"Subject:Price alert\n\nPrice of the product you're watchingn has dropped below your threshold. Current price: ${price}", from_addr=ADDR, to_addrs="disposable38125@yahoo.com")


