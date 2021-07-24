# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: rotate.py
# @description: Rotates coordinates about given vectors

import numpy as np
import scipy as sp
from scipy.spatial.transform import Rotation as R

from typing import Tuple

class Rotate:

  def __init__(self, coordinate: coordinate.Coordinate):
    self.coordinate = coordinate

  def aboutXAxis(self, rotation: float) -> coordinate.Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the X axis

    rotation: float
      The angle (in degrees) to rotate
    """
    pass

  def aboutYAxis(self, rotation: float) -> coordinate.Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the Y axis

    rotation: float
      The angle (in degrees) to rotate
    """
    pass

  def aboutZAxis(self, rotation: float) -> coordinate.Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the Z axis

    rotation: float
      The angle (in degrees) to rotate
    """
    pass

  def aboutVector(self, aboutvec: Tuple[float, float, float], rotation: float) -> coordinate.Coordinate:
    """
    Rotate the input coordinate a given number of degrees around the given vector

    aboutvec: Tuple[float, float, float]
      The vector about which to rotate
    rotation: float
      The angle (in degrees) to rotate
    """
    pass
