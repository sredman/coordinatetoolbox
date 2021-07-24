#!/usr/bin/env python3

import unittest

from src.coordinates import *

class TestCartesian2D(unittest.TestCase):

    def test_constructor(self):
        val = cartesian2D.Cartesian2D(1, 2)
        self.assertEqual(val.x, 1)
        self.assertEqual(val.y, 2)
        self.assertTrue(issubclass(type(val), coordinate.Coordinate), "All coordinate types should be subclasses of Coordinate")

class TestCartesian3D(unittest.TestCase):

    def test_constructor(self):
        val = cartesian3D.Cartesian3D(1, 2, 3)
        self.assertEqual(val.x, 1)
        self.assertEqual(val.y, 2)
        self.assertEqual(val.z, 3)
        self.assertTrue(issubclass(type(val), coordinate.Coordinate), "All coordinate types should be subclasses of Coordinate")

class TestPolar(unittest.TestCase):

    def test_constructor(self):
        val = polar.Polar(1, 45)
        self.assertEqual(val.r, 1)
        self.assertEqual(val.theta, 45)
        self.assertTrue(issubclass(type(val), coordinate.Coordinate), "All coordinate types should be subclasses of Coordinate")

class TestSpherical(unittest.TestCase):

    def test_constructor(self):
        val = spherical.Spherical(1, 45, 45)
        self.assertEqual(val.rho, 1)
        self.assertEqual(val.theta, 45)
        self.assertEqual(val.phi, 45)
        self.assertTrue(issubclass(type(val), coordinate.Coordinate), "All coordinate types should be subclasses of Coordinate")

if __name__ == '__main__':
    unittest.main()
