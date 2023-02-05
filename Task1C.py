'''In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x. 
The required function signature is:
            def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.'''

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run(): #Mary
    
    stations = build_station_list() 
    centre = (52.2053, 0.1218)
    r = 10

    rad = stations_within_radius(stations, centre, r)   #Returns a list that calculates the distance from each station to Cambridge
                                                        #using Haversine, include thoses within r km...
                                                        

    print(f'Stations within {r} km from Cambridge centre: ')
    print(sorted(rad)) #...and sorts entries from closest to furthest

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()


    

    


