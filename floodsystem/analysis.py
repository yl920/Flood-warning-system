import numpy as np
import matplotlib.dates
#Andy
def polyfit(dates, levels, p):#computes a least-squares fit of a polynomial of degree p to water level data
    x = matplotlib.dates.date2num(dates)
    large = x[0] #the shift to account for error, since the number of days from the start of calender is very large
    pcof=np.polyfit(x - large, levels, p) #Using shifted x values, find coefficient of best-fit
    poly = np.poly1d(pcof)# Convert coefficient into a polynomial that can be evaluated
    return poly, large #returns the coefficient for the polynomial, and the shift in days
