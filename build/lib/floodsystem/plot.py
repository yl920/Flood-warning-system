import matplotlib.pyplot as plt
from .analysis import polyfit
import matplotlib

def plot_water_levels(station, dates, levels):
    # Plot labels
    plt.plot(dates, levels, label='water data level')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    
    #include typical low and high levels
    if station.typical_range_consistent():
        plt.axhline(y=station.typical_range[1], label="high", color = 'r',linestyle='-')
        plt.axhline(y=station.typical_range[0], label ="low", color = 'y',linestyle='-')
    plt.legend()

    #display plot
    plt.tight_layout()  
    plt.show()

#Andy
def plot_water_level_with_fit(station, dates, levels, p):
    pcof, large = polyfit(dates, levels, p) #pcof = the coefficients for polynomial; large = shift in days to avoid error
    x = matplotlib.dates.date2num(dates)

    # Plot water level data and best fit polynomial
    plt.plot(dates, pcof(x - large), label = f"least-squares fit of a polynomial of degree {p}")
    plot_water_levels(station, dates, levels)
    
    return
