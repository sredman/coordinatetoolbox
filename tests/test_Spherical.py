#!/usr/bin/env python3
# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: TestSpherical.py
# @description: Test cases for the Spherical coordinate type

import unittest
import math

from src.coordinates import *
from src import convert

class TestSpherical(unittest.TestCase):
  """
  Test cases for the Spherical coordinate type
  """

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

  def test_convert_fromCartesian2D(self):
    """
    Test that converting from Cartesian2D to Spherical correctly returns an error
    """
    val = cartesian2D.Cartesian2D(1, 1)
    with self.assertRaises(convert.ConvertNotDefinedError):
      convert.Convert(val).toSpherical()

  def test_convert_fromCartesian3D(self):
    """
    Test that converting from Cartesian3D to Spherical returns correctly
    """
    val = cartesian3D.Cartesian3D(1, 1, 1)
    expected = spherical.Spherical(math.sqrt(3), 45.0000, 54.7356)
    result = convert.Convert(val).toSpherical()
    self.assertAlmostEqual(expected.rho, result.rho, places=3)
    self.assertAlmostEqual(expected.theta, result.theta, places=3)
    self.assertAlmostEqual(expected.phi, result.phi, places=3)

  def test_convert_fromPolar(self):
    """
    Test that converting from Polar to Spherical correctly returns an error
    """
    val = polar.Polar(1, 45)
    with self.assertRaises(convert.ConvertNotDefinedError):
      convert.Convert(val).toSpherical()

  def test_convert_fromSpherical(self):
    """
    Test that converting from Spherical to Spherical is a no-op
    """
    val = spherical.Spherical(1, 45, 45)
    result = convert.Convert(val).toSpherical()
    self.assertEqual(val, result, "Expected converting spherical coordinates to spherical coordinates to return an equal coordinate")

if __name__ == '__main__':
    unittest.main()
