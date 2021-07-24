# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: spherical.py
# @description: Represent a spherical point

from typing import NamedTuple

from . import coordinate

class Spherical(NamedTuple):
  rho: float
  theta: float
  phi: float

  def __eq__(self, other):
    if not isinstance(other, type(self)):
      return False
    if other is None:
      return False
    return list(self) == list(other)

  def __ne__(self, other):
    return not self.__eq__(other)

coordinate.Coordinate.register(Spherical)
