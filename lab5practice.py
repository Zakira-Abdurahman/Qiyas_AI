import requests
from bs4 import BeautifulSoup

#extract quote text and author name

url ="https://quotes.toscrape.com"

response = requests.get(url)
html=response.text

soup = BeautifulSoup(html, "html.parser")
quotes = soup.find_all("div", class_="quote")
for q in quotes:
    text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text

    print(text)
    print("-", author)
    print("-" * 40)
