import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs4

# Mengambil halaman Wikipedia yang berisi daftar negara berdasarkan benua
continents_page = requests.get("https://simple.wikipedia.org/wiki/List_of_countries_by_continents").text
continents_countries_soup = bs4(continents_page, "lxml")

# Menentukan kata-kata yang tidak diinginkan (misalnya Notes, References, dll)
unwanted_words = ["Notes", "References", "Other website"]

# Menemukan semua heading benua (biasanya dalam tag <h2> yang berisi nama benua)
continents = continents_countries_soup.find_all('h2' > 'div', {"class" : "mw-heading mw-heading2"})

# Memfilter benua yang tidak diinginkan
target_continents = [continent.text for continent in continents if continent.text not in unwanted_words]
# print("Continents")

# Menampilkan benua yang ditemukan
# print("Continents:", target_continents)

# Mengambil semua tabel dengan daftar negara (biasanya dalam <tbody> untuk setiap benua)
ol_html = continents_countries_soup.find_all('tbody')

# Daftar untuk menyimpan negara-negara berdasarkan benua
countries_in_continents = []

# Mengambil nama-nama negara dari setiap tabel
for tbody in ol_html:
    countries = []
    rows = tbody.find_all('tr')

    # Untuk setiap baris (tr), kita ambil negara yang ada di dalam tag <a>
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 2:  # Pastikan ada setidaknya 2 kolom
            country_link = cells[2].find('a')  # Negara biasanya berada di kolom kedua (index 1)
            if country_link:
                country_name = country_link.text
                countries.append(country_name)

    countries_in_continents.append(countries)
#    print(countries)

# Menampilkan hasilnya
#for continent, countries in zip(target_continents, countries_in_continents):
#    print(f"{continent}:")
#    for country in countries:
#        print(f"- {country}")

countries_continents_category_df = pd.DataFrame(zip(countries_in_continents, target_continents), columns=['Country', 'Continent'])
print(countries_continents_category_df)
