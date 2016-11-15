#!/usr/bin/env python

from drawit import Image, Point, PPM, RED, GREEN, BLUE

image = Image()

# Big Red
image.draw_rectangle(
    Point(0, 0),
    Point(image.width - 1, image.height - 1),
    RED
)

# Medium Green
image.draw_rectangle(
    Point(  image.width / 5,   image.height / 5),
    Point(4*image.width / 5, 4*image.height / 5),
    GREEN
)

# Small Blue
image.draw_rectangle(
    Point(  image.width / 3,   image.height / 3),
    Point(2*image.width / 3, 2*image.height / 3),
    BLUE
)

PPM.write(image)

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
