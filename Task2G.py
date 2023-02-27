from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
import datetime
import matplotlib.dates
from floodsystem.station import *

def run():
    no_data = []#create empty list of stations with different catergories
    low = []
    moderate = []
    high = [] 
    severe = []
    stations = build_station_list()
    update_water_levels(stations)
    threshold_severe = 1.2 #threshold
    threshold_high = 1.05
    threshold_mod = 80

    for station in stations:#calculate range with typical data
        if station.typical_range_consistent() and station.latest_level is not None:

            # The function that calculates the risk of flooding is as follows: 
            # it takes the percentage difference between what the water level at the station is now 
            # and the averaged water level at the station over the last 24 hours

            # If the percentage of water level is compared to the previous day:
            # >120%  - severe risk
            # 105% - 120%  - high risk
            # 80% - 105% - moderate risk
            # <80% - low risk

            percentage = station.relative_water_level(station.latest_level)

            # Some stations have .town = None
            # Only include these stations if the flood warning is high/severe
            if station.town is None and percentage >= 1.2:
                station.town = f"The following station does not have data: {station.name}"

            if station.town in severe:
                pass
            elif station.town in high:
                if percentage >= threshold_severe:
                    severe.append(station.town)
                    high.remove(station.town)
            elif station.town in moderate:
                if percentage >= threshold_severe:
                    severe.append(station.town)
                    moderate.remove(station.town)
                elif percentage >= threshold_high:
                    high.append(station.town)
                    moderate.remove(station.town)
            elif station.town in low:
                if percentage >= threshold_severe:
                    severe.append(station.town)
                    low.remove(station.town)
                elif percentage >= threshold_high:
                    high.append(station.town)
                    low.remove(station.town)
                elif percentage >= threshold_mod:
                    moderate.append(station.town)
                    low.remove(station.town)
            else:
                if percentage >= threshold_severe:
                    severe.append(station.town)
                elif percentage >= threshold_high:
                    high.append(station.town)
                elif percentage >= threshold_mod:
                    moderate.append(station.town)
                elif percentage < threshold_mod:
                    low.append(station.town)
                else: no_data.append(station.town)
        else:
            pass
        
        # For stations identified as high risk, estimate if water level
        # is rising or falling using the polyfit best fit function
        # Then, if water level rising, upgrade warning level to severe
        if station.town in high:
            try:
                # Create best-fit polynomial to approximate water level data over past 5 days
                measure_id = station.measure_id
                dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=5))
                bestfit, offset = polyfit(dates, levels, p=4)
                derivative = np.polyder(bestfit) # Differentiate best-fit polynomial
                # Estimate if water level rising or falling at the most recent data point
                gradient = derivative(matplotlib.dates.date2num(dates[0]) - offset) # Evaluate gradient
                # Gradients which are positive but close to 0 are ignored here
                if gradient > 1:
                    high.remove(station.town)
                    severe.append(station.town)
            # Some stations have faulty data - no useful polynomial fit, so leave in current warning category
            except IndexError:
                pass
            except KeyError:
                pass
    
    severe.sort()
    high.sort()

    print(f"Severe Risk:\n{severe}\n")
    print(f"High Risk:\n{high}\n")
    print(f"Moderate Risk:\n{len(moderate)} towns\n")
    print(f"Low Risk:\n{len(low)} towns\n")
    print(f"No Reliable Data:\n{len(no_data)} towns\n")

if __name__ == "__main__":
    run()