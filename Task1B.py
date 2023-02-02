from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
data = build_station_list()
f = (52.2053, 0.1218)
print(stations_by_distance(data, (52.2053, 0.1218)))