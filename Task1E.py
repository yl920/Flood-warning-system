'''
Implement a function in geo that determines the N rivers with 
the greatest number of monitoring stations. 
It should return a list of (river name, number of stations) tuples, 
sorted by the number of stations. 
In the case that there are more rivers with the same number of stations as the N th entry,
 include these rivers in the list. 
'''

from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def rivers_by_station_number(stations, N):
    stations = build_station_list()
    
