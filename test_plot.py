import matplotlib.pyplot as plt
from floodsystem.plot import *
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
from matplotlib.dates import num2date
from floodsystem.stationdata import MonitoringStation

class TestClass:
    def test_plot_water_levels(self): #Mary 2E
        station1 = MonitoringStation(station_id='test_station_id_1',
                                     measure_id='test_measure_id_1',
                                     label='Test Station 1',
                                     coord=(0., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_1',
                                     town='test_town_1')
        station2 = MonitoringStation(station_id='test_station_id_2',
                                     measure_id='test_measure_id_2',
                                     label='Test Station 2',
                                     coord=(1., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_2',
                                     town='test_town_2')
        station3 = MonitoringStation(station_id='test_station_id_3',
                                     measure_id='test_measure_id_3',
                                     label='Test Station 3',
                                     coord=(1., 1.),
                                     typical_range=(0., 1.),
                                     river='test_river_3',
                                     town='test_town_3')
        stations = (station1, station2, station3)
        dates = np.empty(5, dtype=object)
        levels = np.empty(5, dtype=object)
        dt = 10
        for i in range(len(stations)):
            dates[i], levels[i] = fetch_measure_levels(
                stations[i].measure_id, dt=datetime.timedelta(days=dt))

            plot_water_levels(stations[i], dates[i], levels[i])

        assert plt.show() == None
