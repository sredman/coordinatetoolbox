# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: cartesian3D.py
# @description: Represent a 3D Cartesian point

from typing import NamedTuple

from . import coordinate

class Cartesian3D(NamedTuple):
  x: float
  y: float
  z: float

  def __eq__(self, other):
    if not isinstance(other, type(self)):
      return False
    if other is None:
      return False
    return list(self) == list(other)

  def __ne__(self, other):
    return not self.__eq__(other)

coordinate.Coordinate.register(Cartesian3D)
