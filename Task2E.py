from floodsystem.datafetcher import fetch_measure_levels 
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    #highest 5 stations
    N = 5
    highest_5_stations = stations_highest_rel_level(stations, N)  

    #plot water levels over past 10 days for 5 highest stations
    dt = 10

    for station in highest_5_stations:
        measure_id = station.measure_id
        dates, levels = fetch_measure_levels(measure_id, dt)
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()    


