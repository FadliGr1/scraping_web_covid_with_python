
print('\n')
print('\n')
print('000000000              0000000000')
print('000000000000        0000000000000')
print('00000000000000    000000000000000')
print('000000000000000000000000000000000')
print('             00000               ')
print('00000000000         000000000000                      TUGAS BESAR PEMROGRAMAN FUNGSIONAL             ')
print('0000000000000      0000000000000             STUDI KASUS THE FUNCTIONAL APPROACH TO WEB SERVICES     ')
print('     000000000    000000000               ===========================================================')
print('      00000000    00000000                     Name  :  FADLI GUNAWAN RIZQIANTO     ')
print('      00000000    00000000                     Name  :  Dimas Dwi Priyono           ')
print('      00000000    00000000                     Name  :  Muhammad Fatkhul Allam Ulya ')
print('      00000000    00000000')
print('      00000000    00000000')
print('      00000000    00000000')
print('      00000000    00000000')
print('      00000000    00000000')
print('      00000000    00000000')


import requests
from bs4 import BeautifulSoup
import pandas as pd
import dask.dataframe as dd

print('\n')

print('Realtime Data Covid-19 Internasional')

r = requests.get('https://www.worldometers.info/coronavirus')
print('status :', r.status_code, 'OK')

print("Loading... ")
soup = BeautifulSoup(r.content, 'lxml')

table = soup.find('table', attrs={'id': 'main_table_countries_today'})
rows = table.find_all("tr", attrs={"style": ""})

r = []
for i, item in enumerate(rows):
    if i == 0:
        r.append(item.text.strip().split("\n")[:13])
    else:
        r.append(item.text.strip().split("\n")[:12])

print('proses scraping...')

dt = pd.DataFrame(r)
dt = pd.DataFrame(r[1:], columns=r[0][:12])
df = dd.from_pandas(dt,npartitions=1)
df.head()

data = df.to_csv('data-covid-19-*.csv')
print('data tersimpan di :', data)

print('\n')
print('Program Selesai')