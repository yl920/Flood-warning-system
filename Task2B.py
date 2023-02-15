'''Provide a program file Task2B.py that prints the name of each station 
at which the current relative level is over 0.8, with the relative level 
alongside the name (do not forget to handle the cases of inconsistent range data).'''

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    
    stations = build_station_list()
    update_water_levels(stations)

    tol = 0.8
    s=stations_level_over_threshold(stations, tol)

    for station in s:
        print(station[0], station[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()





