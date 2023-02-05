'''In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x. 
The required function signature is:
            def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.'''


from floodsystem.geo import *
from test_station import *


def run():
    station = test_create_monitoring_station()
    new = rivers_with_station(station)
    print(new)
run()