# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from floodsystem.utils import sorted_by_key  # noqa
from .utils import *
from .station import *

#from haversine import haversine, Unit


from math import asin, sqrt, sin, cos, radians
#Haversine function calculates the distance between 2 tuples p and coord of each station and returns a tuple
def haversine(a, b):
    r = 6371
    a_lat, a_lng = a[0], a[1]
    b_lat, b_lng = b[0], b[1]

    return 2 * r * asin(
        sqrt(sin(radians((b_lat - a_lat) / 2)) ** 2
             + cos(radians(a_lat))
             * cos(radians(b_lat))
             * sin(radians((b_lng - a_lng) / 2)) ** 2
             )
    )


### 1C ###
def stations_within_radius(stations, centre, r):
    
    stations_in = []

    for station in stations:
        centre_distance = haversine(centre, station.coord)
        if centre_distance <= r:
            stations_in.append(station.name)
    return stations_in

    ### 1B ###
def stations_by_distance(stations, p):   
#Create new list "list"
#For each loop the name, town and distance for each station is produced as a tuple
#these tuples are appended into the list "list"
    list = [(station.name, station.town, haversine(station.coord, p)) for station in stations]
#Sort the list by its 3rd entry in each tuple, i.e. its distance
    return sorted_by_key(list,2)


### 1D ###
def rivers_with_station(stations):

    #create a list from station to rivers
    rivers = []

    for station in stations:
        if station.river not in rivers:
            rivers.append(station.river)

    return sorted(rivers)


def stations_by_river(stations):
    #create a library from river to station
    river_stations = {}

    for station in stations:
        if station.river not in river_stations.key():
            river_stations[station.river] = [station.name] #add station with new river to the lib
        else:
            river_stations[station.river].append (station.name)

    return river_stations  


### 1E ###

def rivers_by_station_number(stations, N):
    
    river_dict = stations_by_river(stations)
    
    rivers_station = []
    for river in river_dict:
        n = len(river_dict[river])  #number of stations in each river
        rivers_station.append(river, n)


    #compare the n to find the greatest
    greatest = 0

    for river in rivers_station:
        if river[1] > greatest:
            greatest = river[1]
        else:
            greatest = greatest

    #add rivers to the list
    rivers = []

    while len(rivers) < N:
        for n in rivers_station:
            if n[1]  == greatest:
                rivers.append(n)
        greatest -= 1

    return rivers