# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: convert.py
# @description: Convert coordinates between various coordinate systems

import math

from .coordinates import *

class Convert:

  def __init__(self, coordinate: coordinate.Coordinate):
    self.coordinate = coordinate

  def toSpherical(self) -> spherical.Spherical:
    if isinstance(self.coordinate, spherical.Spherical):
      return self.coordinate
    if isinstance(self.coordinate, cartesian3D.Cartesian3D):
      magnitude = math.sqrt(self.coordinate.x**2 + self.coordinate.y**2 + self.coordinate.z**2)
      return spherical.Spherical(
          rho=magnitude,
          theta=math.degrees(math.atan(self.coordinate.y / self.coordinate.x)),
          phi=math.degrees(math.acos(self.coordinate.z / magnitude))
        )

    raise ConvertNotDefinedError("Cannot convert from {type} to {target}".format(type=self.coordinate.__class__.__name__, target=spherical.Spherical.__name__))

class ConvertNotDefinedError(TypeError):
  """
  Error indicating that the conversion requested is not defined (for instance, Cartesian2D to Cartesian3D)
  """
  pass
