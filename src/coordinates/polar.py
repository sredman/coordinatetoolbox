# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

from typing import NamedTuple

from . import coordinate

class Polar(NamedTuple):
  """
  Represent a Polar point in 2D space
  """

  r: float
  theta: float

  def __eq__(self, other):
    if not isinstance(other, type(self)):
      return False
    if other is None:
      return False
    return list(self) == list(other)

  def __ne__(self, other):
    return not self.__eq__(other)

coordinate.Coordinate.register(Polar)
