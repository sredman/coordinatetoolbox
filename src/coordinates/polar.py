# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: polar.py
# @description: Represent a polar point

from typing import NamedTuple

from . import coordinate

class Polar(NamedTuple):
  r: float
  theta: float

coordinate.Coordinate.register(Polar)
