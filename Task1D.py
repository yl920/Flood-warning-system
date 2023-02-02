from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    stations = build_station_list()
    riz = rivers_with_station(stations) #List of rivers that have at least one monitoring station
    print(f"Number of rivers that have at least one monitoring station: {len(riz)}")
    print(f"First 10 -  {list(riz)[:10]}") #Print the first 10 names in the set
    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()