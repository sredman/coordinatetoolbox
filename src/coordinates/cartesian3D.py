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

coordinate.Coordinate.register(Cartesian3D)