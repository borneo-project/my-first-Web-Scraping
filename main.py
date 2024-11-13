import requests
import pandas
import seaborn
import matplotlib.pyplot
from bs4 import BeautifulSoup

continents_page = requests.get("https://simple.wikipedia.org/wiki/List_of_countries_by_continents").text
continents_countries_soup = BeautifulSoup(continents_page, 'html.parser')
continents = continents_countries_soup.find_all('h2' > 'span', {"class":"mw-heading mw-heading2"})
unwanted_word = ["Antartica","Notes","References","Other website"]
target_continents = [continents.text for continents in continents if continents.text not in unwanted_word]
print(continents)


