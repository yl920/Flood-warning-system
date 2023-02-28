from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
import datetime
import matplotlib.dates
from floodsystem.station import *
#Andy
def run():
    null = []#create empty list of stations with different catergories
    low = []
    mod = []
    high = [] 
    severe = []
    stations = build_station_list()
    update_water_levels(stations)
    
    #This part sets the thresholds
    threshold_severe = float(input("Please input a percentage of the original water level that would be considered severe: _____%"))/100
    #obtains the precentage of the threshold, for which the original level is compared to the typical value over the last 24 hours
    if threshold_severe < 0: #filter out invalid numbers
        print("Please enter a valid value!!!")
        quit()
    else:
        pass
    threshold_high = float(input("Please do the same for high threshold: _____%"))/100
    if threshold_high < 0 or threshold_high>threshold_severe:
        print("Please enter a valid value!!!")
        quit()
    else:
        pass
    amogus = float(input("Please do the same for moderate threshold: _____%"))
    threshold_mod = amogus/100
    if threshold_mod < 0 or threshold_mod>threshold_high:
        print("Please enter a valid value!!!")
        quit()

    else:
        pass
    print(f"According to the data you entered, the threshold for low risk is below {amogus}%.")

    #This part creates lists according to the entered thresholds
    for station in stations:#calculate range with typical data
        if station.typical_range_consistent() and station.latest_level is not None: #filter out inconsistent data
            rel=station.relative_water_level(station.latest_level)
            subject = station.town
            # Some stations have .town = None
            # Only include these stations if the flood warning is high/severe
            if subject is None and rel >= threshold_high: #for stations that have station.town=None and at high or more risk...
                subject = f"The following station does not have data: {station.name}"#...raise warning indicating unnamed at-risk station
            #compares relative water level to the thresholds, and sorts the subject into the appropriate catergories
            if rel >= threshold_severe:
                severe.append(subject)
            elif rel < threshold_severe and rel >= threshold_high:
                high.append(subject)
            elif rel < threshold_high and rel >= threshold_mod:
                mod.append(subject)
            elif rel < threshold_mod:
                low.append(subject)
            elif subject is None and rel < threshold_high:
                null.append(subject)
            else:
                null.append(subject)

        else:
            pass
        
        # For stations identified as high risk, estimate if water level
        # is rising or falling using the polyfit best fit function
        # Then, if water level rising, upgrade warning level to severe
        if subject in high:
            try:
                # Create best-fit polynomial to approximate water level data over past 10 days
                measure_id = station.measure_id
                days = 10 #last 10 days
                p = 4 #polynomial of 4th order
                dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days))
                polynomial, offset = polyfit(dates, levels, p) #generate polynomial with data from past 10 days
                gradient = np.polyder(polynomial)(matplotlib.dates.date2num(dates[0]) - offset) #evaluate the first derivative of polynomial and obtain gradient
                #gradients that are greater than 1 indicate a trend for water rising quickly...
                if gradient > 1.0:
                    high.remove(subject)
                    severe.append(subject)#thus promote to severe risk
            #filter out stations with faulty data as they would produce a useless polynomial
            except IndexError or KeyError:
                pass
    
    severe.sort()
    high.sort()
    mod.sort()

    print(f"List of towns at severe risk:\n{severe}\n")
    print(f"List of towns at high risk:\n{high}\n")
    print(f"List of towns at moderate risk::\n{mod}\n")
    print(f"List of towns in low risk:\n{low[:10]} ... and {len(low)-10} other towns\n")
    print(f"Towns with faulty data:\n{len(null)} towns\n")

if __name__ == "__main__":
    run()