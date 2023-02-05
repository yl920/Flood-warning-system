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


    
