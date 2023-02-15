from .utils import sorted_by_key
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    qualified_list = []
    station_in_tol = ()
    for station in stations:
        if MonitoringStation.relative_water_level(station) > tol:
            station_in_tol[0] = station.name
            station_in_tol[1] = MonitoringStation.relative_water_level(station)
        
        qualified_list += station_in_tol
    
    #sort the list by the relative level in descending order
    
    return sorted_by_key(qualified_list, lambda station_in_tol: station_in_tol[1], reverse=True)

    
    