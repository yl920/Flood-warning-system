from floodsystem import stationdata
from .utils import sorted_by_key
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):

    qualified_list = []  #create empty list of tuple

    stationdata.update_water_levels(stations) #update water level

    for station in stations:
        if station.relative_water_level() is not None:  #return none if inconsistent
            if station.relative_water_level() > tol:  #add tuples to the list if satisfying the tol
                station_in_tol = (station.name, station.relative_water_level())  
                qualified_list.append(station_in_tol)

    sorted_list = sorted_by_key(qualified_list, 1, reverse=True)  #sorted by relative water level value in descending order

    return sorted_list   

def stations_highest_rel_level(stations, N):

    stations_relative_level = []

    stationdata.update_water_levels(stations)

    for station in stations:
        if station.relative_water_level(station.latest_level) is not None:
            station_name_water_level = station, station.relative_water_level(station.latest_level)
            stations_relative_level.append(station_name_water_level)

    sorted_stations_relative_level = sorted_by_key(stations_relative_level, 1, reverse=True)[:N]
  
    newlist = []
    for n in sorted_stations_relative_level:
        newlist.append(n[0])

    return newlist