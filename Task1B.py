from floodsystem import geo
from floodsystem.stationdata import build_station_list
data = build_station_list(use_cache=True)
print(geo.stations_by_distance(data, (52.2053, 0.1218)))