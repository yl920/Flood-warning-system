'''In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x. 
The required function signature is:
            def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.'''

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

#geo:
'''
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

#geo)
'''

def run():
    
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10

    within_radius = stations_within_radius(stations, centre, r)

    print(f'Stations within {r} km from Cambridge centre: ')
    print(sorted(within_radius))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()


    

    


