#!/usr/bin/env python3
# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: TestCartesian3D.py
# @description: Test cases for the Cartesian3D coordinate type

import unittest
import math

from src.coordinates.coordinate import Coordinate
from src.coordinates.cartesian2D import Cartesian2D
from src.coordinates.cartesian3D import Cartesian3D
from src.coordinates.polar import Polar
from src.coordinates.spherical import Spherical

from src.convert import Convert, ConvertNotDefinedError

class TestCartesian3D(unittest.TestCase):
  """
  Test cases for the Cartesian3D coordinate type
  """

  def test_constructor(self):
    val = Cartesian3D(1, 2, 3)
    self.assertEqual(val.x, 1)
    self.assertEqual(val.y, 2)
    self.assertEqual(val.z, 3)
    self.assertTrue(issubclass(type(val), Coordinate), "All coordinate types should be subclasses of Coordinate")

  def test_equals_basis(self):
    """
    Test that the equality operator works correctly when given inputs expected to be equal
    """
    val1 = Cartesian3D(1, 2, 3)
    val2 = Cartesian3D(1, 2, 3)
    self.assertEqual(val1, val2)

  def test_equals_false(self):
    """
    Test that the equality operator works correctly when given inputs expected to be not equal
    """
    val1 = Cartesian3D(1, 2, 3)
    val2 = Cartesian3D(2, 1, 3)
    self.assertNotEqual(val1, val2)

  def test_equals_other_type(self):
    """
    Test that the equality operator works correctly when given inputs of different types
    """
    val1 = Cartesian3D(1, 2, 3)
    val2 = Spherical(1, 2, 3)
    # Exercise the __ne__ operator
    self.assertNotEqual(val1, val2)
    # Exercise the __eq__ operator
    self.assertFalse(val1 == val2)

  def test_equals_none(self):
    """
    Test that the equality operator works correctly when given None as an input
    """
    val1 = Cartesian3D(1, 2, 3)
    val2 = None
    # Exercise the __ne__ operator
    self.assertNotEqual(val1, val2)
    # Exercise the __eq__ operator
    self.assertFalse(val1 == val2)

  def test_convert_fromCartesian2D(self):
    """
    Test that converting from Cartesian2D to Cartesian3D correctly returns an error
    """
    val = Cartesian2D(1, 1)
    with self.assertRaises(ConvertNotDefinedError):
      Convert(val).toCartesian3D()

  def test_convert_fromCartesian3D(self):
    """
    Test that converting from Cartesian3D to Cartesian3D is a no-op
    """
    val = Cartesian3D(1, 2, 3)
    expected = Cartesian3D(1, 2, 3)
    result = Convert(val).toCartesian3D()
    self.assertEqual(expected, result, "Expected converting Cartesian3D coordinates to Cartesian3D coordinates to return an equal coordinate")

  def test_convert_fromPolar(self):
    """
    Test that converting from Polar to Cartesian3D correctly returns an error
    """
    val = Polar(1, 45)
    with self.assertRaises(ConvertNotDefinedError):
      Convert(val).toCartesian3D()

  def test_convert_fromSpherical(self):
    """
    Test that converting from Spherical to Cartesian3D returns correctly
    """
    val = Spherical(math.sqrt(3), 45.0000, 54.7356)
    expected = Cartesian3D(1, 1, 1)
    result = Convert(val).toCartesian3D()
    self.assertAlmostEqual(expected.x, result.x, places=3)
    self.assertAlmostEqual(expected.y, result.y, places=3)
    self.assertAlmostEqual(expected.z, result.z, places=3)

if __name__ == '__main__':
    unittest.main()
