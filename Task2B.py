from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8       #set value for tolerance
    stationlist = stations_level_over_threshold(stations, tol) #list satisfying the tol

    print("Stations with a relative water level within tolerance:")
    
    for station in stationlist:
        print(station[0], station[1]) #print separately rather than in tuples

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
