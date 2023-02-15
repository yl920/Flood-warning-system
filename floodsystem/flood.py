'''
from .utils import sorted_by_key
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    qualified_list = []
    station_in_tol = ()
    for station in stations:
        relative_fraction = MonitoringStation.relative_water_level(station)
        if relative_fraction > tol:
            station_in_tol[0] = station.name
            station_in_tol[1] = relative_fraction
        
        qualified_list.append(station_in_tol)
    
    #sort the list by the relative level in descending order
    
    return sorted_by_key(qualified_list, lambda station_in_tol: station_in_tol[1], reverse=True)
'''
from floodsystem import stationdata
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):

    """Returns a list of the tuples, each containing the name of a station at which the relative
        water level is above tol and the relative water level at that station"""

    flooded_stations = []

    stationdata.update_water_levels(stations)

    for station in stations:
        if station.relative_water_level(station.latest_level) is not None:
            if station.relative_water_level(station.latest_level) > tol:
                station_name_water_level = (station, station.relative_water_level(station.latest_level))
                flooded_stations.append(station_name_water_level)

    sorted_flooded_stations = sorted_by_key(flooded_stations, 1, reverse=True)

    return sorted_flooded_stations   
    