import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
#Andy
def run():
    #station list
    stations = build_station_list()
    #5 stations with the highest water level
    N = 5
    highest_waterlevel_stations = stations_highest_rel_level(stations, N)

    dt = 10 #period of days
    p = 4 #degree of polynomial


    for station in highest_waterlevel_stations: #plot each station individually
        try:
            measure_id = station.measure_id
            dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=dt))
            plot_water_level_with_fit(station, dates, levels, p)#water level over time is plotted for the stations
            
        except IndexError: #skip faulty data
            pass

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()