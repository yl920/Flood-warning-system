'''In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x. 
The required function signature is:
            def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.'''

from floodsystem.stationdata import build_station_list

def stations_within_radius(stations, centre, r):
    init_stations = build_station_list()

    for station in init_stations:
        if station.name in stations:
            return station
    
   # if station.


    


