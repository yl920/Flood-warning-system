import matplotlib.pyplot as plt

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

