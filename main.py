import requests
import pandas
import pandas as pd
import seaborn as snn
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs4

continents_page = requests.get("https://simple.wikipedia.org/wiki/List_of_countries_by_continents").text
print(continents_page)
