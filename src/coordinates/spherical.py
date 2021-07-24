# @author: Simon Redman <simon@ergotech.com>
# @date: 2021-07-24
# @filename: spherical.py
# @description: Represent a spherical point

from typing import NamedTuple

class Spherical(NamedTuple):
  rho: float
  theta: float
  phi: float
