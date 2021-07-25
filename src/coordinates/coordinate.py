# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

from abc import ABC

class Coordinate(ABC):
  """
  Abstract parent class for all other coordinate classes

  Use Coordinate.register(OtherType) in the other type's definition file
  to define it as a sub-type of Coordinate
  """
  pass
