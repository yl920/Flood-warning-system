'''
Implement a function in geo that determines the N rivers with 
the greatest number of monitoring stations. 
It should return a list of (river name, number of stations) tuples, 
sorted by the number of stations. 
In the case that there are more rivers with the same number of stations as the N th entry,
 include these rivers in the list. 
'''

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run(): #Mary

    stations = build_station_list() 
    N = 9    # the 9 rivers with greatest number of stations  

    river_station_number = rivers_by_station_number(stations, N)

    print(f'The {N} rivers with greatest number of stations :')
    print(river_station_number)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run() 

    
