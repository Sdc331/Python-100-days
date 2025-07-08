from bs4 import BeautifulSoup
import requests

site_data = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
site_data.encoding = "utf-8"
site_output = site_data.text

soup = BeautifulSoup(site_output, 'html.parser')

titles_obj = soup.find_all("h3", class_="title")
titles = [" ".join(title.getText().split()[1:]) for title in titles_obj]

with open("top100.txt", "a") as f:
    for each in titles:
        f.write(f"{titles.index(each) + 1}. {each}\n")
