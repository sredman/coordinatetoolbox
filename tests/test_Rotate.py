#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

import unittest
import math

from src.coordinates import Coordinate
from src.coordinates import Cartesian2D
from src.coordinates import Cartesian3D
from src.coordinates import Polar
from src.coordinates import Spherical

from src.rotate import Rotate

class TestRotate(unittest.TestCase):
  """
  Test cases for rotations
  """

  def test_rotate_xunit_xaxis(self):
    """
    Test that a rotation of the x unit-vector about the x axis returns correctly
    """
    val = Cartesian3D(1, 0, 0)
    expected = Cartesian3D(1, 0, 0)
    result = Rotate(val).aboutXAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_xunit_yaxis(self):
    """
    Test that a rotation of the x unit-vector about the y axis returns correctly
    """
    val = Cartesian3D(1, 0, 0)
    expected = Cartesian3D(0, 0, -1)
    result = Rotate(val).aboutYAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_xunit_zaxis(self):
    """
    Test that a rotation of the x unit-vector about the z axis returns correctly
    """
    val = Cartesian3D(1, 0, 0)
    expected = Cartesian3D(0, 1, 0)
    result = Rotate(val).aboutZAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_yunit_xaxis(self):
    """
    Test that a rotation of the y unit-vector about the x axis returns correctly
    """
    val = Cartesian3D(0, 1, 0)
    expected = Cartesian3D(0, 0, 1)
    result = Rotate(val).aboutXAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_neg_yunit_xaxis(self):
    """
    Test that a rotation of the negative y unit-vector about the x axis returns correctly
    """
    val = Cartesian3D(0, -1, 0)
    expected = Cartesian3D(0, 0, -1)
    result = Rotate(val).aboutXAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_yunit_yaxis(self):
    """
    Test that a rotation of the y unit-vector about the y axis returns correctly
    """
    val = Cartesian3D(0, 1, 0)
    expected = Cartesian3D(0, 1, 0)
    result = Rotate(val).aboutYAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_yunit_zaxis(self):
    """
    Test that a rotation of the y unit-vector about the z axis returns correctly
    """
    val = Cartesian3D(0, 1, 0)
    expected = Cartesian3D(-1, 0, 0)
    result = Rotate(val).aboutZAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_zunit_xaxis(self):
    """
    Test that a rotation of the z unit-vector about the x axis returns correctly
    """
    val = Cartesian3D(0, 0, 1)
    expected = Cartesian3D(0, -1, 0)
    result = Rotate(val).aboutXAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_zunit_yaxis(self):
    """
    Test that a rotation of the z unit-vector about the y axis returns correctly
    """
    val = Cartesian3D(0, 0, 1)
    expected = Cartesian3D(1, 0, 0)
    result = Rotate(val).aboutYAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_zunit_zaxis(self):
    """
    Test that a rotation of the z unit-vector about the z axis returns correctly
    """
    val = Cartesian3D(0, 0, 1)
    expected = Cartesian3D(0, 0, 1)
    result = Rotate(val).aboutZAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_idvec_xaxis(self):
    """
    Test that a rotation of the identity vector about the x axis returns correctly
    """
    val = Cartesian3D(1, 1, 1)
    expected = Cartesian3D(1, -1, 1)
    result = Rotate(val).aboutXAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_idvec_yaxis(self):
    """
    Test that a rotation of the identity vector about the y axis returns correctly
    """
    val = Cartesian3D(1, 1, 1)
    expected = Cartesian3D(1, 1, -1)
    result = Rotate(val).aboutYAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def test_rotate_idvec_zaxis(self):
    """
    Test that a rotation of the identity vector about the z axis returns correctly
    """
    val = Cartesian3D(1, 1, 1)
    expected = Cartesian3D(-1, 1, 1)
    result = Rotate(val).aboutZAxis(90)
    self.fuzzyCompareCartesian3D(expected, result)

  def fuzzyCompareCartesian3D(self, val1: Cartesian3D, val2: Cartesian3D, places=3):
    self.assertAlmostEqual(val1.x, val2.x, places=places)
    self.assertAlmostEqual(val1.y, val2.y, places=places)
    self.assertAlmostEqual(val1.z, val2.z, places=places)
