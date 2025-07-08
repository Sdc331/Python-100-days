from bs4 import BeautifulSoup
import requests

site_data = requests.get("https://news.ycombinator.com/news")
site_output = site_data.text

soup = BeautifulSoup(site_output, 'html.parser')


# titles = soup.find_all(".titleline")
titles = soup.select(".titleline")
scores = soup.select(".score")
x = 0
for title in titles:
    print(f"{title.a.getText()}\n{title.a.get('href')}")
    print(scores[x].getText())
    x += 1

# print(titles)













# for tag in soup.find_all("a"):
#     # print(tag.getText())
#     print(tag.get("href"))

# print(soup.select_one(selector="p a"))
