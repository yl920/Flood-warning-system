'''In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x. 
The required function signature is:
            def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.'''

from floodsystem.stationdata import build_station_list
import haversine


def stations_within_radius(stations, centre, r):
    stations = build_station_list()

    for station in stations:
        a = station.coord
        centre_distance = haversine(centre, a)        
        if centre_distance <= r:
                return stations.name
    #for station in stations:
       # if station.name in [
        #        'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge'
      #  ]:
      #      print(station)
        

list = ('Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge')
print(stations_within_radius(list, (52.2053, 0.1218), 10))