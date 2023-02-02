from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list



def run():



    stations = build_station_list() 

    new_list = stations_by_distance(stations,(52.2053, 0.1218))
    print('The closest 10 entries are:')
    print(new_list[:10])
    print('The furthest 10 are:')
    print(new_list[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()