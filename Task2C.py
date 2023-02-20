from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10          #greatest 10 relative levels
    station_list = stations_highest_rel_level(stations, N)

    for station in station_list:
        print(station[0], station[1])  #print components

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()