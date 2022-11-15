#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:11:18 2022

@author: skyejung
"""

'''
LAB 5
'''


#%%
## User Input Zipcode

zip = input('Zipcode: ')

#%%
# Convert to Long/Lat

import pgeocode
import requests

nomi = pgeocode.Nominatim('us')
query = nomi.query_postal_code(zip)

lat = query["latitude"]
lon = query["longitude"]
print(lat)
print(lon)

#%%
# scrape 7 Day Forecast & Display

from bs4 import BeautifulSoup

url = ('https://forecast.weather.gov/MapClick.php?lat='+str(lat)+'&lon='+str(lon)+'#.Y2wSMOzMK3I')
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id='seven-day-forecast')
forecast_items = seven_day.find_all(class_='tombstone-container')
tonight = forecast_items[0]
# print(tonight.prettify())

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
# print(short_descs)

import pandas as pd
weather = pd.DataFrame({
 "period": periods,
 "short_desc": short_descs,
 "temp": temps,
 "desc":descs
})
weather

#%%
# Display Currebt Conditions

currentid = soup.find(id='current_conditions_detail')
# print(currentid.prettify())


string = str(currentid.find(class_='').get_text())
string = string.split('\n')
humidity = string[3]
wind_speed = string[7]
dew_point = string[15]
last_update = string[24]

current_condition = ({
 "humidity": humidity,
 "wind_speed": wind_speed,
 "dew_point": dew_point,
 "last_update_time": last_update
})
current_condition

#%%
# Store in MongoDB

import pymongo
import pprint
import pandas as pd

host_name = "localhost"
port = "27017"

atlas_cluster_name = "sandbox"
atlas_default_dbname = "local"
atlas_user_name = "m001-student"
atlas_password = "m001-mongodb-basics"

conn_str = {
    "local" : f"mongodb://{host_name}:{port}/",
    "atlas" : f"mongodb+srv://{atlas_user_name}:{atlas_password}@{atlas_cluster_name}.zibbf.mongodb.net/{atlas_default_dbname}"
}

client = pymongo.MongoClient(conn_str["local"])

db_name = "store_weather"

db = client[db_name]
collection_forecast = db["7_day_forecast"]
collection_conditions = db["current_conditions"]

item1 = {"period": periods,
 "short_desc": short_descs,
 "temp": temps,
 "desc":descs}

item2 = {"humidity": humidity,
 "wind_speed": wind_speed,
 "dew_point": dew_point,
 "last_update_time": last_update}

collection_forecast.insert_one(item1)
collection_conditions.insert_one(item2)

print("Collections: ", db.list_collection_names())

pprint.pprint(collection_forecast.find_one({}))
pprint.pprint(collection_conditions.find_one({}))