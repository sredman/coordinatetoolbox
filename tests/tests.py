#!/usr/bin/env python3

import unittest

from src.coordinates import *

class TestCartesian2D(unittest.TestCase):

    def test_constructor(self):
        val = cartesian2D.Cartesian2D(1, 2)
        self.assertEqual(val.x, 1)
        self.assertEqual(val.y, 2)
        self.assertTrue(issubclass(type(val), coordinate.Coordinate), "All coordinate types should be subclasses of Coordinate")

    def test_equals_basis(self):
      """
      Test that the equality operator works correctly when given inputs expected to be equal
      """
      val1 = cartesian2D.Cartesian2D(1, 2)
      val2 = cartesian2D.Cartesian2D(1, 2)
      self.assertEqual(val1, val2)

    def test_equals_false(self):
      """
      Test that the equality operator works correctly when given inputs expected to be not equal
      """
      val1 = cartesian2D.Cartesian2D(1, 2)
      val2 = cartesian2D.Cartesian2D(2, 1)
      self.assertNotEqual(val1, val2)

    def test_equals_other_type(self):
      """
      Test that the equality operator works correctly when given inputs of different types
      """
      val1 = cartesian2D.Cartesian2D(1, 2)
      val2 = polar.Polar(1, 2)
      # Exercise the __ne__ operator
      self.assertNotEqual(val1, val2)
      # Exercise the __eq__ operator
      self.assertFalse(val1 == val2)

    def test_equals_none(self):
      """
      Test that the equality operator works correctly when given None as an input
      """
      val1 = cartesian2D.Cartesian2D(1, 2)
      val2 = None
      # Exercise the __ne__ operator
      self.assertNotEqual(val1, val2)
      # Exercise the __eq__ operator
      self.assertFalse(val1 == val2)

class TestCartesian3D(unittest.TestCase):

    def test_constructor(self):
        val = cartesian3D.Cartesian3D(1, 2, 3)
        self.assertEqual(val.x, 1)
        self.assertEqual(val.y, 2)
        self.assertEqual(val.z, 3)
        self.assertTrue(issubclass(type(val), coordinate.Coordinate), "All coordinate types should be subclasses of Coordinate")

    def test_equals_basis(self):
      """
      Test that the equality operator works correctly when given inputs expected to be equal
      """
      val1 = cartesian3D.Cartesian3D(1, 2, 3)
      val2 = cartesian3D.Cartesian3D(1, 2, 3)
      self.assertEqual(val1, val2)

    def test_equals_false(self):
      """
      Test that the equality operator works correctly when given inputs expected to be not equal
      """
      val1 = cartesian3D.Cartesian3D(1, 2, 3)
      val2 = cartesian3D.Cartesian3D(2, 1, 3)
      self.assertNotEqual(val1, val2)

    def test_equals_other_type(self):
      """
      Test that the equality operator works correctly when given inputs of different types
      """
      val1 = cartesian3D.Cartesian3D(1, 2, 3)
      val2 = spherical.Spherical(1, 2, 3)
      # Exercise the __ne__ operator
      self.assertNotEqual(val1, val2)
      # Exercise the __eq__ operator
      self.assertFalse(val1 == val2)

    def test_equals_none(self):
      """
      Test that the equality operator works correctly when given None as an input
      """
      val1 = cartesian3D.Cartesian3D(1, 2, 3)
      val2 = None
      # Exercise the __ne__ operator
      self.assertNotEqual(val1, val2)
      # Exercise the __eq__ operator
      self.assertFalse(val1 == val2)

class TestPolar(unittest.TestCase):

    def test_constructor(self):
        val = polar.Polar(1, 45)
        self.assertEqual(val.r, 1)
        self.assertEqual(val.theta, 45)
        self.assertTrue(issubclass(type(val), coordinate.Coordinate), "All coordinate types should be subclasses of Coordinate")

    def test_equals_basis(self):
      """
      Test that the equality operator works correctly when given inputs expected to be equal
      """
      val1 = polar.Polar(1, 45)
      val2 = polar.Polar(1, 45)
      self.assertEqual(val1, val2)

    def test_equals_false(self):
      """
      Test that the equality operator works correctly when given inputs expected to be not equal
      """
      val1 = polar.Polar(1, 45)
      val2 = polar.Polar(2, 45)
      self.assertNotEqual(val1, val2)

    def test_equals_other_type(self):
      """
      Test that the equality operator works correctly when given inputs of different types
      """
      val1 = polar.Polar(1, 45)
      val2 = cartesian2D.Cartesian2D(1, 45)
      # Exercise the __ne__ operator
      self.assertNotEqual(val1, val2)
      # Exercise the __eq__ operator
      self.assertFalse(val1 == val2)

    def test_equals_none(self):
      """
      Test that the equality operator works correctly when given None as an input
      """
      val1 = polar.Polar(1, 45)
      val2 = None
      # Exercise the __ne__ operator
      self.assertNotEqual(val1, val2)
      # Exercise the __eq__ operator
      self.assertFalse(val1 == val2)

class TestSpherical(unittest.TestCase):

    def test_constructor(self):
        val = spherical.Spherical(1, 45, 45)
        self.assertEqual(val.rho, 1)
        self.assertEqual(val.theta, 45)
        self.assertEqual(val.phi, 45)
        self.assertTrue(issubclass(type(val), coordinate.Coordinate), "All coordinate types should be subclasses of Coordinate")

    def test_equals_basis(self):
      """
      Test that the equality operator works correctly when given inputs expected to be equal
      """
      val1 = spherical.Spherical(1, 45, 45)
      val2 = spherical.Spherical(1, 45, 45)
      self.assertEqual(val1, val2)

    def test_equals_false(self):
      """
      Test that the equality operator works correctly when given inputs expected to be not equal
      """
      val1 = spherical.Spherical(1, 45, 45)
      val2 = spherical.Spherical(1, 135, 45)
      self.assertNotEqual(val1, val2)

    def test_equals_other_type(self):
      """
      Test that the equality operator works correctly when given inputs of different types
      """
      val1 = spherical.Spherical(1, 45, 45)
      val2 = cartesian3D.Cartesian3D(1, 45, 45)
      # Exercise the __ne__ operator
      self.assertNotEqual(val1, val2)
      # Exercise the __eq__ operator
      self.assertFalse(val1 == val2)

    def test_equals_none(self):
      """
      Test that the equality operator works correctly when given None as an input
      """
      val1 = spherical.Spherical(1, 45, 45)
      val2 = None
      # Exercise the __ne__ operator
      self.assertNotEqual(val1, val2)
      # Exercise the __eq__ operator
      self.assertFalse(val1 == val2)

if __name__ == '__main__':
    unittest.main()
