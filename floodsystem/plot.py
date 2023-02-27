'''
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
'''
import matplotlib.pyplot as plt
def plot_water_levels(station, dates, levels):
    # Plot
    plt.plot(dates, levels, label='water data level')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()  
    if station.typical_range_consistent():
        plt.axhline(y=station.typical_range[1], label="high", color = 'r',linestyle='-')
        plt.axhline(y=station.typical_range[0], label ="low", color = 'y',linestyle='-')
    plt.legend()

    plt.show()

