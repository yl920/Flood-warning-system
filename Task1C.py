'''In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x. 
The required function signature is:
            def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.'''

from floodsystem.stationdata import build_station_list
import math

def stations_within_radius(stations, centre, r):
    init_stations = build_station_list()

    for station in init_stations:
        if station.name in stations:
            return station
        centre_distance = math.sqrt((station.coord [1] - centre[1])^2 + (station.coord [0] - centre[0])^2)
        if centre_distance <= r:
            return station.name
        

list = ('Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge')
print(stations_within_radius(list, (52.2053, 0.1218), 10))


    

    


