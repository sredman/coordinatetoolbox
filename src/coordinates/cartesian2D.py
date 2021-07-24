# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: cartesian2D.py
# @description: Represent a 2D Cartesian point

from typing import NamedTuple

from . import coordinate

class Cartesian2D(NamedTuple):
  x: float
  y: float

coordinate.Coordinate.register(Cartesian2D)
