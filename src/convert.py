# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

import math

from .coordinates.coordinate import Coordinate
from .coordinates.spherical import Spherical
from .coordinates.cartesian3D import Cartesian3D

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
      return Spherical(
          rho=magnitude,
          theta=math.degrees(math.atan(self.coordinate.y / self.coordinate.x)),
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
