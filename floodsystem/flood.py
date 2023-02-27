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

    stations_rel_level = []

    stationdata.update_water_levels(stations)

    for station in stations:
        if station.relative_water_level() is not None:
            name_and_level = (station.name, station.relative_water_level()) #tuples of station name and rel water level
            stations_rel_level.append(name_and_level)

    sorted_n_stations_rel_level = sorted_by_key(stations_rel_level, 1, reverse=True)[:N]  #sort by relative water level in descending order and get greatest N
  
    return sorted_n_stations_rel_level