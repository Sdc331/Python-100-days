import requests, datetime, smtplib, os

COMPANY_NAME = "TSLA"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TO_MAIL = "disposable38125@yahoo.com"
FROM_MAIL = os.environ.get("MY_MAIL")
MAIL_KEY = os.environ.get("ADDR_PASS")



TODAY = datetime.datetime.today().date()
DAY_ONE = str(TODAY - datetime.timedelta(days=3))
DAY_TWO = str(TODAY - datetime.timedelta(days=4))

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": COMPANY_NAME,
    "apikey": STOCK_API_KEY,
}
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "country": "us",
    "q": "tesla",
    "pageSize": 3,
}

def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0

with requests.get(NEWS_API_ENDPOINT, news_parameters) as req:
    req.raise_for_status()
    data = req.json()
articles = []
if data["totalResults"] == 0:
    articles.append("There are no articles available online")
else:
    for each in data["articles"]:
        articles.append(f"Headline: {each['title']}\nLink: {each['url']}\n")

with requests.get(STOCK_API_ENDPOINT, parameters) as req:
    req.raise_for_status()
    output = req.json()

day_one_open = float(output["Time Series (Daily)"][DAY_ONE]["1. open"])
day_two_open = float(output["Time Series (Daily)"][DAY_TWO]["1. open"])

result = round(get_change(day_one_open, day_two_open), 2)
if result >= 1:
    if day_one_open >= day_two_open:
        change = f"{COMPANY_NAME}:^%{result}"
    elif day_two_open >= day_one_open:
        change = f"{COMPANY_NAME}:v%{result} "

final_message = f"{change}\n"
for each in articles:
    final_message += each

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(FROM_MAIL, MAIL_KEY)
    connection.sendmail(from_addr=FROM_MAIL, to_addrs=TO_MAIL, msg=f"Subject:Daily stock info\n\n{final_message}")

## STEP 3: Use smtplib
# Send a seperate mail with the percentage change and each article's title and description to your email. 



