import matplotlib 
from .station import MonitoringStation
import matplotlib.pyplot as plt

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

