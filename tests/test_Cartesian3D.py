#!/usr/bin/env python3
# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: TestCartesian3D.py
# @description: Test cases for the Cartesian3D coordinate type

import unittest

from src.coordinates.coordinate import Coordinate
from src.coordinates.cartesian2D import Cartesian2D
from src.coordinates.cartesian3D import Cartesian3D
from src.coordinates.polar import Polar
from src.coordinates.spherical import Spherical

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

if __name__ == '__main__':
    unittest.main()
