from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run(): #Mary
    stations = build_station_list()
    inconsistent_data = inconsistent_typical_range_stations(stations)
    
    inconsistent_station_names = []

    for station in inconsistent_data:
        inconsistent_station_names.append(station.name)

    print('Stations with inconsistent data: ')
    print(sorted(inconsistent_station_names))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()