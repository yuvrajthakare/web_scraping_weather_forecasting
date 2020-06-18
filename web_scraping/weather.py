import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=36.17193000000003&lon=-115.14000999999996#.XgCRy_kza00")
soup = BeautifulSoup(page.content , 'html.parser')
#print(soup)

week = soup.find(id='seven-day-forecast-body')

#print(week)

items = week.find_all(class_='tombstone-container')

'''
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
'''
period_name = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temprature = [item.find(class_='temp').get_text() for item in items]

'''
print(period_name)
print(short_description)
print(temprature)
'''

weather_stuff  = pd.DataFrame(
    {
        'period' : period_name,
        'short_description' : short_description,
        'temprature' : temprature,
    }
)
print(weather_stuff)

weather_stuff.to_csv('weather.csv')