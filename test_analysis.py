import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy

def test_polyfit():
    stationlist = build_station_list() #Build list with 10 entries from station list with dates and levels
    for station in stationlist[:10]:
        measure_id = station.measure_id
        dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=5))

        output = polyfit(dates, levels, 4) #gives the set of data
        assert isinstance(output, tuple) #check the output is of tuple, etc.
        assert isinstance(output[0], numpy.poly1d)
        assert isinstance(output[1], float)
        assert len(output) == 2 #check output only 2 items in tuple