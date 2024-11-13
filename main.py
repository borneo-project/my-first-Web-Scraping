import requests
import pandas as pd
import seaborn as snn
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

continents_page = requests.get("https://simple.wikipedia.org/wiki/List_of_countries_by_continents").text
continents_page

continents_countries_soup = bs4(continents_page,"html")
continents = continents_countries_soup.find_all('h2' > 'span', {"class":"mw-heading mw-heading2"})
continents