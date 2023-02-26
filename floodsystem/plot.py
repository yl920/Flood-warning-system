import matplotlib.pyplot as plt
import matplotlib 
from .station import MonitoringStation

from .analysis import *

def plot_water_levels(station, dates, levels):

    #plot
    plt.plot(dates, levels, label = "water level data")

    #Add axis labels, title
    plt.title(station.name)
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)

    #plot typical high/low levels
    high = [station.typical_range[1]] * len(levels)
    low = [station.typical_range[0]] * len(levels)
    plt.plot(dates, high, '--',label = "typical high level")
    plt.plot(dates, low, 'g--',label = "typical low level")   
    plt.legend()
    
    #display plot
    plt.tight_layout()

    plt.show
    
    return

def plot_water_level_with_fit(station, dates, levels, p):
    """Display water level data alongside best-fit polynomial"""
    poly, offset = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)

    # Plot water level data and best fit polynomial
    plt.plot(dates, poly(x - offset), label = "best fit polynomial")
    plot_water_levels(station, dates, levels)
    
    return

