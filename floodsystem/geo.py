# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#from floodsystem.stationdata import build_station_list

#from .utils import sorted_by_key  # noqa
import operator
from haversine import haversine, Unit
list=[]
def stations_by_distance(stations, p):
    for i in  stations:
        station_name = i["Station name"]
        coords = i["coordinate"]
        d = haversine(p,coords)
        list.append(())
        list(len(list)-1).append(station_name)
        list(len(list)-1).append(d)
    sorted_by_key(list,1)

#print(stations_by_distance())