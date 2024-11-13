import requests
from bs4 import BeautifulSoup

# URL halaman Wikipedia yang berisi daftar negara berdasarkan benua
url = "https://simple.wikipedia.org/wiki/List_of_countries_by_continents"

# Mengambil konten halaman
response = requests.get(url)
response.raise_for_status()  # Mengecek jika ada kesalahan saat request

# Mem-parse HTML menggunakan BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Menghapus elemen "legend", "see also", "notes", dan "references"
# Kita akan mencari elemen-elemen tersebut berdasarkan id atau class tertentu dan menghapusnya
for element in soup.find_all(['div', 'ul', 'span']):
    # Memeriksa apakah elemen memiliki atribut 'class'
    if 'class' in element.attrs:
        if 'reflist' in element['class']:  # Menghapus daftar referensi
            element.decompose()
        if 'hatnote' in element['class']:  # Menghapus "see also" dan catatan lainnya
            element.decompose()

# Menghapus elemen lain berdasarkan ID (misalnya, bagian "Notes" dan "References")
for element in soup.find_all(id=['References', 'See_also', 'Notes']):
    element.decompose()

# Mencari semua header benua (biasanya menggunakan <h2>)
headers = soup.find_all('h2')

# Menyimpan hasil scraping
countries_by_continent = {}

# Loop untuk memproses tiap header benua
for header in headers:
    # Cek apakah header ini berisi nama benua
    continent_name = header.get_text(strip=True)

    # Jika nama benua ditemukan (misalnya 'Africa', 'Asia', dll.), ambil tabel negara di bawahnya
    if continent_name and continent_name not in countries_by_continent:
        # Menemukan tabel yang berada di bawah header benua tersebut
        next_node = header.find_next_sibling()
        countries = []

        # Cek apakah node berikutnya adalah tabel
        while next_node and next_node.name != 'h2':  # Jika kita belum menemukan header benua lainnya
            if next_node.name == 'table' and 'wikitable' in next_node.get('class', []):
                # Ambil baris tabel dan ekstrak nama negara
                rows = next_node.find_all('tr')[1:]  # Abaikan header tabel
                for row in rows:
                    columns = row.find_all('td')
                    if len(columns) > 1:
                        country_name = columns[1].get_text(strip=True)  # Nama negara di kolom kedua
                        if country_name:  # Pastikan nama negara tidak kosong
                            countries.append(country_name)
            next_node = next_node.find_next_sibling()

        # Simpan negara-negara yang ditemukan untuk benua ini
        countries_by_continent[continent_name] = countries

# Menampilkan hasil
for continent, countries in countries_by_continent.items():
    print(f"{continent}:")
    for country in countries:
        print(f" - {country}")
    print("\n")