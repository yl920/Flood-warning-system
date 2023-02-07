from floodsystem.geo import *
from floodsystem.stationdata import *
from test_station import *
import pytest
class TestClass:

    def test_stations_by_distance(self): #Task B
        one = MonitoringStation(station_id='test_station_id_1',
                                        measure_id='test_measure_id_1',
                                        label='Test Station 1',
                                        coord=(0., 1.),
                                        typical_range=(0., 1.),
                                        river='test_river_1',
                                        town='test_town_1')
        two = MonitoringStation(station_id='test_station_id_2',
                                        measure_id='test_measure_id_2',
                                        label='Test Station 2',
                                        coord=(1., 1.),
                                        typical_range=(0., 1.),
                                        river='test_river_2',
                                        town='test_town_2')
        stations = [one, two]
        new = stations_by_distance(stations, (0., 0.))
        assert new[0][0:2] == ('Test Station 1', 'test_town_1')
        assert new[1][0:2] == ('Test Station 2', 'test_town_2')

    def test_haversine(self): #Task C
        assert haversine((0., 0.), (0., 0.)) == 0.0
        assert round(haversine((0., 0.), (1., 1.)), 1) == 157.2
        assert round(haversine((0., 0.), (6.9, 8.008)), 1) == 1173.8
    
    def test_stations_within_radius(self):
        alpha = MonitoringStation(station_id='test_station_id_1',
                                        measure_id='test_measure_id_1',
                                        label='Daniel River',
                                        coord=(52.9, -2.3),
                                        typical_range=(0., 1.),
                                        river='america river',
                                        town='test_town_1')
        beta = MonitoringStation(station_id='test_station_id_2',
                                        measure_id='test_measure_id_2',
                                        label='Test Station 2',
                                        coord=(1., 1.),
                                        typical_range=(0., 1.),
                                        river='sus river',
                                        town='test_town_2')
        stations = [alpha,beta]
        centre = (52.956914213623556, -2.313288018832415)
        r = 69
        new = stations_within_radius(stations,centre, r)
        assert new == ['Daniel River']

    def test_rivers_with_station(self): #Task D
        alpha = MonitoringStation(station_id='test_station_id_1',
                                        measure_id='test_measure_id_1',
                                        label='Test Station 1',
                                        coord=(52.9, -2.3),
                                        typical_range=(0., 1.),
                                        river='america river',
                                        town='test_town_1')
        beta = MonitoringStation(station_id='test_station_id_2',
                                        measure_id='test_measure_id_2',
                                        label='Test Station 2',
                                        coord=(1., 1.),
                                        typical_range=(0., 1.),
                                        river='sus river',
                                        town='test_town_2')
        stations = [alpha, beta]
        new = rivers_with_station(stations)
        assert new == ['america river','sus river']
    def test_stations_by_river(self): #Task D
        alpha = MonitoringStation(station_id='test_station_id_1',
                                        measure_id='test_measure_id_1',
                                        label='Test Station 1',
                                        coord=(0., 1.),
                                        typical_range=(0., 1.),
                                        river='america river',
                                        town='test_town_1')
        beta = MonitoringStation(station_id='test_station_id_2',
                                        measure_id='test_measure_id_2',
                                        label='Test Station 2',
                                        coord=(1., 1.),
                                        typical_range=(0., 1.),
                                        river='sus river',
                                        town='test_town_2')
        stations = [alpha, beta]
        new = stations_by_river(stations)
        assert new == {"america river":["Test Station 1"],"sus river":["Test Station 2"]}

    """def test_rivers_by_station_number(self):  #Test Task E
        station1 = MonitoringStation(station_id="111",
                                     measure_id="111",
                                     label="Station 1",
                                     coord=(0, 1),
                                     typical_range=(0.1, 0.4),
                                     river="River 1",
                                     town="Town 1")
        station2 = MonitoringStation(station_id="222",
                                     measure_id="222",
                                     label="Station 2",
                                     coord=(1, 1),
                                     typical_range=(0.3, 0.8),
                                     river="River 2",
                                     town="Town 2")
        station3 = MonitoringStation(station_id="333",
                                     measure_id="333",
                                     label="Station 3",
                                     coord=(0, 3),
                                     typical_range=(0.43, 0.88),
                                     river="River 2",
                                     town="Town 3")
        station4 = MonitoringStation(station_id="444",
                                     measure_id="444",
                                     label="Station 4",
                                     coord=(8, 3),
                                     typical_range=(0.1, 0.9),
                                     river="River 3",
                                     town="Town 4")
        assert rivers_by_station_number([station1], 1) == [("River 1", 1)]
        assert rivers_by_station_number([station1, station2, station3], 1) == [("River 2", 2)]
        assert rivers_by_station_number([station1, station2, station3], 2) == [("River 2", 2), ("River 1", 1)]
        assert rivers_by_station_number([station1, station2, station3, station4], 2) == [("River 2", 2), ("River 1", 1),
                                                                                         ("River 3", 1)]
        assert rivers_by_station_number([station1, station2, station3, station4], 3) == [("River 2", 2), ("River 1", 1),
                                                                                         ("River 3", 1)]
        assert rivers_by_station_number([station1, station2, station3, station4], 4) == [("River 2", 2), ("River 1", 1),
                                                                                         ("River 3", 1)]
        assert rivers_by_station_number([station1, station2, station3, station4], 5) == [("River 2", 2), ("River 1", 1),
                                                                                         ("River 3", 1)]"""

    
