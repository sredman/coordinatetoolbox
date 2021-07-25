# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: rotate.py
# @description: Rotates coordinates about given vectors

import math
import numpy as np
import scipy as sp
from scipy.spatial.transform import Rotation as R

from typing import Tuple

from .convert import Convert
from .coordinates.coordinate import Coordinate
from .coordinates.spherical import Spherical
from .coordinates.cartesian3D import Cartesian3D

class Rotate:

  def __init__(self, coordinate: Coordinate):
    self.coordinate = coordinate

  def aboutXAxis(self, rotation: float) -> Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the X axis

    rotation: float
      The angle (in degrees) to rotate
    """
    return self.aboutVector(aboutvec=[1, 0, 0], rotation=rotation)

  def aboutYAxis(self, rotation: float) -> Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the Y axis

    rotation: float
      The angle (in degrees) to rotate
    """
    return self.aboutVector(aboutvec=[0, 1, 0], rotation=rotation)

  def aboutZAxis(self, rotation: float) -> Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the Z axis

    rotation: float
      The angle (in degrees) to rotate
    """
    return self.aboutVector(aboutvec=[0, 0, 1], rotation=rotation)

  def aboutVector(self, aboutvec: Tuple[float, float, float], rotation: float) -> Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the given vector

    aboutvec: Tuple[float, float, float]
      The vector about which to rotate
    rotation: float
      The angle (in degrees) to rotate
    """
    rotvec = R.from_rotvec(math.radians(rotation) * np.array(aboutvec))
    input = Convert(self.coordinate).toCartesian3D()
    outvec = rotvec.apply(input)
    retval = Cartesian3D(outvec[0], outvec[1], outvec[2])

    # Now convert that output back to what the user actually wanted to rotate
    if isinstance(self.coordinate, Spherical):
      return Convert(retval).toSpherical();
    if isinstance(self.coordinate, Cartesian3D):
      return Convert(retval).toCartesian3D();
    raise NotImplementedError("Not prepared to rotate a {type}".format(self.coordinate.__class__.__name__));
