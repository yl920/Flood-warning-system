'''In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x. 
The required function signature is:
            def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.'''

from floodsystem.stationdata import build_station_list
import haversine

def stations_within_radius(stations, centre, r):
    init_stations = build_station_list()

    for station in init_stations:
        if station.name in stations:
            centre_distance = haversine(centre, station.coord)
            if centre_distance <= r:
                return station.name
            

        
        

list = ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
print(stations_within_radius(list, (52.2053, 0.1218), 10))


    

    


