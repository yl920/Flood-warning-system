# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
import pytest

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

    s_id = "test-a-id"
    m_id = "test-a-id"
    label = "alpha station"
    coord = (-2.1, 6.3)
    trange = (-2.3, 3.4445)
    river = "River Asparagus"
    town = "Among Town"
    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert a.station_id == s_id
    assert a.measure_id == m_id
    assert a.name == label
    assert a.coord == coord
    assert a.typical_range == trange
    assert a.river == river
    assert a.town == town