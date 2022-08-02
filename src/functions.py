from pymongo import MongoClient
import numpy as np
import pandas as pd
import time
import requests
import sys


# setup specific to my console, my dataset
client = MongoClient("localhost:27017")
client.list_database_names()

db = client["Ironhack"]
db.list_collection_names()
c = db.get_collection("companies")


# Create a dataframe for all offices in the city
def find_offices(city):
    
    # set parameters for list discovery
    filter_ = {"offices.city":city}
    projection = {"_id":0, "name":1, "offices.city":1, "offices.latitude":1, "offices.longitude":1}
    
    # pass all offices into this dict
    name = []
    lat = []
    lon = []

    # loop through each company
    for i in list(c.find(filter_, projection)):    

        # loop through each office in a company
        for y in i['offices']:
            
            # only add values if this is the correct city branch of the company
            if y['city'] == city:
            
                # add mongo values to a dictionary
                name.append(i['name'])
                lat.append(y['latitude'])
                lon.append(y['longitude'])

    # apply new info to a dictionary, then to a dataframe
    to_df = {'name':name, 'lat':lat, 'lon':lon}
    df = pd.DataFrame.from_dict(to_df)
    df.dropna(inplace=True)
    
    #df.reset_index()
    numbers = range(0, len(df))
    df['numbers'] = numbers
    df = df.set_index('numbers')
    df.index.name = None

    return df

# search for a given venue with the shortest distance to each location in a given dataframe
def get_venue(venue, df):
    # store values in lists to be added to the passed df
    name = []
    distance = []
    lat = []
    lon = []
    
    # 
    for i in range(len(df)):
        url = f"https://api.foursquare.com/v3/places/search?query={venue}&ll={df['lat'][i]}%2C{df['lon'][i]}&sort=DISTANCE&limit=1"
        headers = {
            "Accept": "application/json",
            "Authorization": "fsq3nSb08fmNysRWqCGqA/6XjzbUkx+LGcB+JOstG+sNUI8="
        }
        response = requests.get(url, headers=headers)
        name.append(df['name'][i])
        distance.append(response.json()["results"][0]['distance'])
        lat.append(response.json()["results"][0]["geocodes"]['main']['latitude'])
        lon.append(response.json()["results"][0]["geocodes"]['main']['longitude'])
    
    # apply new info to a dictionary, then to a dataframe
    to_df = {'name':name, f'{venue} distance':distance, f'{venue} lat':lat, f'{venue} lon':lon}
    df = pd.DataFrame.from_dict(to_df)
    
    return df

# return the office location with the lowest (ranked) distance from all requirements
def closest_office(city):
    lowest_score = sys.maxsize
    lowest_coords = []
    for i in city.index.values.tolist():
        sum_of_weighted_distances = city.at[i,'startup distance']*1185 + city.at[i,'design distance']*765 + city.at[i,'starbucks distance']*600 
        + city.at[i,'school distance']*765 + city.at[i,'club distance']*510 + city.at[i,'stadium distance']*275 + city.at[i,'vegan distance']*80 + city.at[i,'pet services distance']*25
        if city.at[i,'airport distance'] > 20000: # check if airport is too far away (longer than 45 min taxi/20km)
            sum_of_weighted_distances =0
        if sum_of_weighted_distances < lowest_score:
            lowest_score = sum_of_weighted_distances
            while len(lowest_coords) > 0:
                lowest_coords.pop()
            lowest_coords.append([city.at[i,'lat'], city.at[i,'lon']])
    return lowest_coords
