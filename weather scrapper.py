from bs4 import BeautifulSoup
import requests
from collections import deque

file=open("weather.txt","w")

def Weather( link ):
    response=requests.get(link)
    soup=BeautifulSoup(response.text,'lxml')
    seven_days=soup.find(id='seven-day-forecast')
    forecast_items = seven_days.find_all(class_="tombstone-container")
    #print(forecast_items)
    tonight=forecast_items[0]
    #print(tonight)
    #print(tonight.prettify())
    for items in forecast_items:
        period=items.find(class_='period-name')
        image_title=items.find('img')
        short=items.find(class_='short-desc')
        temp=items.find(class_='temp')
        file.write(period.get_text()+'\n')
        file.write(image_title.get('title')+'\n')
        file.write(short.get_text()+'\n')
        file.write(temp.get_text()+"\n\n")

Link="https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
Weather(Link)
file.close()
