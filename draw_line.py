#!/usr/bin/env python

from drawit import Image, Point, PPM, RED, GREEN, BLUE, WHITE

import math

image       = Image()
center      = Point(image.width / 2, image.height / 2)
radius      = min(image.width, image.height) / 2 - 1
colors      = [RED, GREEN, BLUE]
color_index = 0
angle       = 0

# Draw lines from center
while angle <= (2*math.pi):
    edge = Point(center.x + radius*math.cos(angle),
                 center.y + radius*math.sin(angle))

    image.draw_line(center, edge, colors[color_index % len(colors)])
    image[edge] = WHITE

    angle       += math.pi / 32
    color_index += 1

# Write image to stdout
PPM.write(image)

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
