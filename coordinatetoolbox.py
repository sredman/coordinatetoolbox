#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Simon Redman <simon@ergotech.com>
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

"""
Interactive entry-point for Coordinate Toolbox
"""

import argparse
from argparse import HelpFormatter

from src.coordinates import Cartesian3D

from src.rotate import Rotate
from src.convert import Convert

class CustomHelpFormatter(HelpFormatter):
  """
  Help formatter for Coordinate Toolbox
  """

  def _format_action_invocation(self, action):
    if not action.option_strings:
      # Use default methods for positional arguments
      default = self._get_default_metavar_for_positional(action)
      metavar, = self._metavar_formatter(action, default)(1)
      return metavar
    parts = []
    if action.nargs == 0:
      # Just add options, if they expects no values (like --help)
      parts.extend(action.option_strings)
    else:
      default = self._get_default_metavar_for_optional(action)
      args_string = self._format_args(action, default)
      for option_string in action.option_strings:
        parts.append(option_string)
      # Join the argument names (like -p --param ) and add the metavar at the end
      return '%s %s' % (', '.join(parts), args_string)
    return ', '.join(parts)

def main():
  """
  Main method for Coordinate Toolbox CLI
  """

  parser = argparse.ArgumentParser(
    description='Toolbox for converting between coordinate systems and rotating points in 3D space',
    formatter_class=CustomHelpFormatter
    )
  parser.add_argument('-v', '--version',
                      action='version',
                      version='coordinatetoolbox 1.0'
                      )
  parser.add_argument('-i', '--input',
                      metavar='float',
                      type=float,
                      nargs=3,
                      help='Input point, like --input x y z',
                      required=True
                      )
  parser.add_argument('-r', '--rotation',
                      metavar='float',
                      type=float,
                      help='Angle in degrees to rotate',
                      default=0
                      )
  parser.add_argument('-a', '--axis',
                      choices=['x', 'y', 'z'],
                      type=str,
                      help='Axis about which to rotate',
                      default='x'
                      )
  parser.add_argument('-os', '--output-system',
                      choices=['cartesian3D', 'spherical'],
                      help='Coordinate system to use for outputs',
                      default='spherical'
                      )
  args = parser.parse_args()

  input_coordinate = Cartesian3D(*args.input)

  rotated = None
  if args.axis == 'x':
    rotated = Rotate(input_coordinate).about_x_axis(args.rotation)
  if args.axis == 'y':
    rotated = Rotate(input_coordinate).about_y_axis(args.rotation)
  if args.axis == 'z':
    rotated = Rotate(input_coordinate).about_z_axis(args.rotation)

  output = None
  if args.output_system == 'cartesian3D':
    output = Convert(rotated).toCartesian3D()
  if args.output_system == 'spherical':
    output = Convert(rotated).toSpherical()

  print(output)

if __name__ == "__main__":
  main()
