from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
import datetime
import matplotlib.dates
from floodsystem.station import *

def run():
    null = []#create empty list of stations with different catergories
    low = []
    mod = []
    high = [] 
    severe = []
    stations = build_station_list()
    update_water_levels(stations)
    threshold_severe = float(input("severe")) #threshold
    threshold_high = float(input("high"))
    threshold_mod = float(input("mod"))
    print("placeholder")
    for station in stations:#calculate range with typical data
        if station.typical_range_consistent() and station.latest_level is not None: #filter out inconsistent data

            # The function that calculates the risk of flooding is as follows: 
            # it takes the percentage difference between what the water level at the station is now 
            # and the averaged water level at the station over the last 24 hours

            # If the percentage of water level is compared to the previous day:
            # >120%  - severe risk
            # 105% - 120%  - high risk
            # 80% - 105% - moderate risk
            # <80% - low risk

            rel=station.relative_water_level(station.latest_level)
            subject = station.town
            # Some stations have .town = None
            # Only include these stations if the flood warning is high/severe
            if subject is None and rel >= threshold_high: #for stations that have station.town=None and at high or more risk...
                subject = f"The following station does not have data: {station.name}"#...raise warning indicating unnamed at-risk station
            if rel >= threshold_severe:
                severe.append(subject)
            elif rel < threshold_severe and rel >= threshold_high:
                high.append(subject)
            elif rel < threshold_high and rel >= threshold_mod:
                mod.append(subject)
            elif rel < threshold_mod:
                low.append(subject)
            else:
                null.append(subject)
            """
            if subject in severe:#if the subject is already labelled severe, move on...
                pass
            elif subject in high:
                if rel >= threshold_severe:#if the subject exceeds severe threshold, remove from high and add to severe
                    severe.append(subject)
                    high.remove(subject)
            elif subject in mod:
                if rel >= threshold_severe:#if the subject exceeds severe threshold, remove from moderate and add to severe
                    severe.append(subject)
                    mod.remove(subject)
                elif rel >= threshold_high:#...similar to above
                    high.append(subject)
                    mod.remove(subject)
            elif subject in low:
                if rel >= threshold_severe:
                    severe.append(subject)
                    low.remove(subject)
                elif rel >= threshold_high:
                    high.append(subject)
                    low.remove(subject)
                elif rel >= threshold_mod:
                    mod.append(subject)
                    low.remove(subject)
            else:#if subject is not already placed in a list, 
                if rel >= threshold_severe:#...still the same
                    severe.append(subject)
                elif rel >= threshold_high:
                    high.append(subject)
                elif rel >= threshold_mod:
                    mod.append(subject)
                elif rel < threshold_mod:#if the subject is not in any list but still is not None, that implies subject has value lower than moderate threshold and placed in low risk
                    low.append(subject)
                else: null.append(subject)#otherwise append subject to list with faulty data
                """
        else:
            pass
        
        # For stations identified as high risk, estimate if water level
        # is rising or falling using the polyfit best fit function
        # Then, if water level rising, upgrade warning level to severe
        if subject in high:
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
                    high.remove(subject)
                    severe.append(subject)
            # Some stations have faulty data - no useful polynomial fit, so leave in current warning category
            except IndexError:
                pass
            except KeyError:
                pass
    
    severe.sort()
    high.sort()

    print(f"Severe Risk:\n{severe}\n")
    print(f"High Risk:\n{high}\n")
    print(f"Moderate Risk:\n{len(mod)} towns\n")
    print(f"Low Risk:\n{len(low)} towns\n")
    print(f"No Reliable Data:\n{len(null)} towns\n")

if __name__ == "__main__":
    run()