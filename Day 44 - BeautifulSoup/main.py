from bs4 import BeautifulSoup

with open("website.html") as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')
# for tag in soup.find_all("a"):
#     # print(tag.getText())
#     print(tag.get("href"))

print(soup.select_one(selector="p a"))