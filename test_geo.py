from floodsystem.geo import *
from floodsystem.stationdata import *
from test_station import *
# import pytest
class TestClass:

    def test_stations_by_distance(self): #Task B Andy
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

    def test_haversine(self): #Task C Andy
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

    def test_rivers_with_station(self): #Task D Andy
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
    def test_stations_by_river(self): #Task D Andy
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

     #Test Task E
    def test_rivers_by_station_number(self):
        s_id = "test-s-id"
        m_id = "test-m-id"
        label = "station"
        coord = (1, 1)
        trange = None
        river1 = "River 1"
        river2 = "River 2"
        river3 = "River 3"
        river4 = "River 4"
        town = "Town"
        s1 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
        s2 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
        s3 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
        s4 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
        s5 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
        s6 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
        s7 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
        s8 = MonitoringStation(s_id, m_id, label, coord, trange, river4, town)
        stations = [s1, s2, s3, s4, s5, s6, s7, s8]

        assert len(rivers_by_station_number(stations, 1)) == 1
        river_list = rivers_by_station_number(stations, 2)
        assert len(river_list) == 3
        assert "River 4" not in [item[0] for item in river_list]

        for river in ["River 1", "River 2", "River 3"]:
            assert river in [item[0] for item in river_list]