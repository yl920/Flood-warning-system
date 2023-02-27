import matplotlib.pyplot as plt
from floodsystem.plot import *
from floodsystem.station import *
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from matplotlib.dates import num2date

from floodsystem.stationdata import build_station_list, update_water_levels

def test_plot_water_levels(): #Mary 2E
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[15] #randomly pick a station to plot
    dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=10))
    plot_water_levels(station, dates, levels)
    plt.close()        

test_plot_water_levels()