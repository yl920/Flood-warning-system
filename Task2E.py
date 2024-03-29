
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels


def sorts(station):
    if not station.relative_water_level():
        return 0.0
    return station.relative_water_level()


def run():
    stations = build_station_list()
    update_water_levels(stations)
    #sort stations by relative water levels
    stations.sort(key=sorts, reverse=True)
    #highest 5 stations
    count = 0
    for station in stations:
        #plot water levels over past 10 days for 5 highest stations
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if dates:
            plot_water_levels(station, dates, levels)
            count = count + 1
        if count == 5:
            break

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()  