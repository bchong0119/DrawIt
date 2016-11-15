#!/usr/bin/env python

from drawit import Image, Point, PPM, RED, GREEN, BLUE

image  = Image()
center = Point(image.width / 2, image.height / 2)
radius = min(image.width, image.height) / 2 - 1

# Big Red
image.draw_circle(center, radius, RED)

# Medium Green
image.draw_circle(center, radius/2, GREEN)

# Small Blue
image.draw_circle(center, radius/4, BLUE)

# Write image to stdout
PPM.write(image)

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
