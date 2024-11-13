import requests
from bs4 import BeautifulSoup

# URL halaman Wikipedia yang berisi daftar negara berdasarkan benua
url = "https://simple.wikipedia.org/wiki/List_of_countries_by_continents"

# Mengambil konten halaman
response = requests.get(url)
response.raise_for_status()  # Mengecek jika ada kesalahan saat request

# Mem-parse HTML menggunakan BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Mencari tabel yang berisi data negara berdasarkan benua
# Di halaman ini, kita tahu bahwa tabel-tabel negara berdasarkan benua terdapat dalam <table> dengan class "wikitable"
tables = soup.find_all('h2' > 'span', {"class":"mw-heading mw-heading2"})


# Menyimpan hasil scraping
countries_by_continent = {}

# Loop untuk memproses tiap tabel
for table in tables:
    # Mendapatkan nama benua dari header tabel
    header = table.find_previous('h2').text.strip()
    continent_name = header.split(' ')[0]  # Mengambil nama benua (misalnya "Afrika", "Asia", dll.)

    # List untuk menyimpan nama negara
    countries = []

    # Mengambil semua baris dalam tabel
    rows = table.find_all('tr')[1:]  # Mengabaikan heade

print(tables)