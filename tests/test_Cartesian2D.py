#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

import unittest

from src.coordinates import Coordinate
from src.coordinates import Cartesian2D
from src.coordinates import Cartesian3D
from src.coordinates import Polar
from src.coordinates import Spherical

class TestCartesian2D(unittest.TestCase):
  """
  Test cases for the Cartesian2D coordinate type
  """

  def test_constructor(self):
    val = Cartesian2D(1, 2)
    self.assertEqual(val.x, 1)
    self.assertEqual(val.y, 2)
    self.assertTrue(issubclass(type(val), Coordinate), "All coordinate types should be subclasses of Coordinate")

  def test_equals_basis(self):
    """
    Test that the equality operator works correctly when given inputs expected to be equal
    """
    val1 = Cartesian2D(1, 2)
    val2 = Cartesian2D(1, 2)
    self.assertEqual(val1, val2)

  def test_equals_false(self):
    """
    Test that the equality operator works correctly when given inputs expected to be not equal
    """
    val1 = Cartesian2D(1, 2)
    val2 = Cartesian2D(2, 1)
    self.assertNotEqual(val1, val2)

  def test_equals_other_type(self):
    """
    Test that the equality operator works correctly when given inputs of different types
    """
    val1 = Cartesian2D(1, 2)
    val2 = Polar(1, 2)
    # Exercise the __ne__ operator
    self.assertNotEqual(val1, val2)
    # Exercise the __eq__ operator
    self.assertFalse(val1 == val2)

  def test_equals_none(self):
    """
    Test that the equality operator works correctly when given None as an input
    """
    val1 = Cartesian2D(1, 2)
    val2 = None
    # Exercise the __ne__ operator
    self.assertNotEqual(val1, val2)
    # Exercise the __eq__ operator
    self.assertFalse(val1 == val2)

if __name__ == '__main__':
  unittest.main()
