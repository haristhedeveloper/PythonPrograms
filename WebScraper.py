from bs4 import BeautifulSoup
import requests

import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

soup.find_all('table')[1]

soup.find('table',class_='wikitable sortable')

table=soup.find_all('table')[1]     

print(table)

worldtitle=table.find_all('th')
print(worldtitle)

worldtable=[title.text.strip() for title in worldtitle]
print(worldtable)

df=pd.DataFrame(columns=worldtable)
df

column_data=table.find_all('tr')

for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row=[data.text.strip() for data in row_data]
    
    length=len(df)
    df.loc[length]=individual_row

df.to_csv('Companies.csv')






