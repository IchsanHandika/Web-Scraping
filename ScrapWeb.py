import requests
from bs4 import BeautifulSoup
import pandas as pd

City = []
Population = []

page = requests.get("https://www.worldometers.info/world-population/japan-population/")
soup = BeautifulSoup(page.content, 'html.parser')

CityName = soup.findAll("td", style = "font-weight: bold; font-size:17px; text-align:left; padding-left:10px; padding-top:5px; padding-bottom:5px" )
Pop = soup.findAll("td", style = " font-size:17px; text-align:left; padding-left:10px; padding-top:5px; padding-bottom:5px")

for x in CityName :
    City.append(x.text)

for y in Pop :
    Population.append(y.text)

df = pd.DataFrame({'City ' : City, '   Population' : Population})
df.to_csv('JPN_Pop.csv', index= False, encoding = 'utf-8')
pd.set_option('display.max_rows', None)
df = pd.read_csv('JPN_Pop.csv')
df
print(df)