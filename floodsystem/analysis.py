import numpy as np
from matplotlib.dates import date2num

def polyfit(dates, levels, p):
    datenum = date2num(dates)
    x = [date - datenum[-1] for date in datenum]
    poly = np.poly1d(np.polyfit(x, levels, p))
    return poly, datenum[-1]
