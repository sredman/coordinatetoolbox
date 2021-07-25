#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

import unittest

from src.coordinates.coordinate import Coordinate
from src.coordinates.cartesian2D import Cartesian2D
from src.coordinates.cartesian3D import Cartesian3D
from src.coordinates.polar import Polar
from src.coordinates.spherical import Spherical

class TestPolar(unittest.TestCase):
  """
  Test cases for the Polar coordinate type
  """

  def test_constructor(self):
    val = Polar(1, 45)
    self.assertEqual(val.r, 1)
    self.assertEqual(val.theta, 45)
    self.assertTrue(issubclass(type(val), Coordinate), "All coordinate types should be subclasses of Coordinate")

  def test_equals_basis(self):
    """
    Test that the equality operator works correctly when given inputs expected to be equal
    """
    val1 = Polar(1, 45)
    val2 = Polar(1, 45)
    self.assertEqual(val1, val2)

  def test_equals_false(self):
    """
    Test that the equality operator works correctly when given inputs expected to be not equal
    """
    val1 = Polar(1, 45)
    val2 = Polar(2, 45)
    self.assertNotEqual(val1, val2)

  def test_equals_other_type(self):
    """
    Test that the equality operator works correctly when given inputs of different types
    """
    val1 = Polar(1, 45)
    val2 = Cartesian2D(1, 45)
    # Exercise the __ne__ operator
    self.assertNotEqual(val1, val2)
    # Exercise the __eq__ operator
    self.assertFalse(val1 == val2)

  def test_equals_none(self):
    """
    Test that the equality operator works correctly when given None as an input
    """
    val1 = Polar(1, 45)
    val2 = None
    # Exercise the __ne__ operator
    self.assertNotEqual(val1, val2)
    # Exercise the __eq__ operator
    self.assertFalse(val1 == val2)

if __name__ == '__main__':
    unittest.main()
