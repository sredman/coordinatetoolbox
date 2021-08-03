# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

"""
Operator class for various rotations on the given coordinate
"""

import math
from typing import Tuple

import numpy as np
from scipy.spatial.transform import Rotation as R

from .convert import Convert
from .coordinates import Coordinate
from .coordinates import Spherical
from .coordinates import Cartesian3D

class Rotate:
  """
  Operator class for various rotations on the given coordinate
  """

  def __init__(self, coordinate: Coordinate):
    self.coordinate = coordinate

  def about_x_axis(self, rotation: float) -> Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the X axis

    rotation: float
      The angle (in degrees) to rotate
    """
    return self.about_vector(aboutvec=[1, 0, 0], rotation=rotation)

  def about_y_axis(self, rotation: float) -> Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the Y axis

    rotation: float
      The angle (in degrees) to rotate
    """
    return self.about_vector(aboutvec=[0, 1, 0], rotation=rotation)

  def about_z_axis(self, rotation: float) -> Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the Z axis

    rotation: float
      The angle (in degrees) to rotate
    """
    return self.about_vector(aboutvec=[0, 0, 1], rotation=rotation)

  def about_vector(self, aboutvec: Tuple[float, float, float], rotation: float) -> Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the given vector

    aboutvec: Tuple[float, float, float]
      The vector about which to rotate
    rotation: float
      The angle (in degrees) to rotate
    """
    rotvec = R.from_rotvec(math.radians(rotation) * np.array(aboutvec))
    invec = Convert(self.coordinate).toCartesian3D()
    outvec = rotvec.apply(invec)
    retval = Cartesian3D(outvec[0], outvec[1], outvec[2])

    # Now convert that output back to what the user actually wanted to rotate
    if isinstance(self.coordinate, Spherical):
      return Convert(retval).toSpherical();
    if isinstance(self.coordinate, Cartesian3D):
      return Convert(retval).toCartesian3D();
    raise NotImplementedError("Not prepared to rotate a {type}".format(self.coordinate.__class__.__name__));
