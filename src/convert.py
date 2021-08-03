# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

import math

from src.coordinates import Coordinate
from src.coordinates import Cartesian3D
from src.coordinates import Spherical

class Convert:
  """
  Operator class for converting between coordinate systems
  """

  def __init__(self, coordinate: Coordinate):
    self.coordinate = coordinate

  def toSpherical(self) -> Spherical:
    if isinstance(self.coordinate, Spherical):
      return self.coordinate
    if isinstance(self.coordinate, Cartesian3D):
      magnitude = math.sqrt(self.coordinate.x**2 + self.coordinate.y**2 + self.coordinate.z**2)
      atan_theta = math.degrees(math.atan(self.coordinate.y / self.coordinate.x))
      # Since arctan only ever returns between -90 and 90 degrees, we need to use our knowledge
      # of geometry to "translate" the angle correctly
      if self.coordinate.x >= 0:
        theta = atan_theta
      elif self.coordinate.x < 0:
        theta = atan_theta + 180

      if theta < 0:
        # Always return a positive value for degrees
        theta = theta + 360

      return Spherical(
          rho=magnitude,
          theta=theta,
          phi=math.degrees(math.acos(self.coordinate.z / magnitude))
        )

    raise ConvertNotDefinedError("Cannot convert from {type} to {target}".format(type=self.coordinate.__class__.__name__, target=Spherical.__name__))

  def toCartesian3D(self) -> Cartesian3D:
    if isinstance(self.coordinate, Cartesian3D):
      return self.coordinate
    if isinstance(self.coordinate, Spherical):
      theta = math.radians(self.coordinate.theta)
      phi = math.radians(self.coordinate.phi)
      return Cartesian3D(
          x=self.coordinate.rho * math.sin(phi) * math.cos(theta),
          y=self.coordinate.rho * math.sin(phi) * math.sin(theta),
          z=self.coordinate.rho * math.cos(phi)
        )

    raise ConvertNotDefinedError("Cannot convert from {type} to {target}".format(type=self.coordinate.__class__.__name__, target=Spherical.__name__))

class ConvertNotDefinedError(TypeError):
  """
  Error indicating that the conversion requested is not defined (for instance, Cartesian2D to Cartesian3D)
  """
  pass
