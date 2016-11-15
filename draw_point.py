#!/usr/bin/env python

from drawit import Image, Point, COLORS, PPM

image        = Image()
column_width = image.width / len(COLORS)

# Draw columns of colors
for y in range(image.height):
    for x in range(image.width):
        image[Point(x, y)] = COLORS[x / column_width % len(COLORS)]

# Write image to stdout
PPM.write(image)

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
