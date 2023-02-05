from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list



def run(): #Andy
    stations = build_station_list() 
#Define a list of station that is sorted by distance to Cambridge
    new_list = stations_by_distance(stations,(52.2053, 0.1218))
    print('The closest 10 entries are:')
#Print the first and last 10 entries respectively
    print(new_list[:10])
    print('The furthest 10 are:')
    print(new_list[-10:])
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()