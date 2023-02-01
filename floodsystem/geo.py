# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
list=[]
def stations_by_distance(stations, p):
    for i in  stations:
        station_name = ["Station name: "]
        coords = ["coordinate: "]
        d = haversine(p,coords)
        list.append(())
        list(len(list)-1).append(station_name)
        list(len(list)-1).append(d)
    sorted_by_key(list,1)


### 1C ###

from math import asin, sqrt, sin, cos, radians

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


def stations_within_radius(stations, centre, r):
    
    stations_in = []

    for station in stations:
        centre_distance = haversine(centre, station.coord)
        if centre_distance <= r:
            stations_in.append(station.name)
    return stations_in