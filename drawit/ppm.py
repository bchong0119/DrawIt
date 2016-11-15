''' ppm.py: DrawIt PPM module '''

from color import Color
from image import Image
from point import Point

import sys

class PPM(object):
    ''' Portable Pixmap

    https://en.wikipedia.org/wiki/Netpbm_format
    '''
    MAGIC     = 'P6'
    MAX_VALUE = 255

    @staticmethod
    def read(path):
        ''' Read PPM image from path '''
        with open(path, 'r') as file:
            magic           = PPM.readline(file)
            width, height   = map(int, PPM.readline(file).split())
            max_value       = int(PPM.readline(file))
            image           = Image(width, height)
            image.magic     = magic
            image.max_value = max_value

            for y in range(image.height):
                for x in range(image.width):
                    image[Point(x, y)] = Color(r=ord(file.read(1)), g=ord(file.read(1)), b=ord(file.read(1)))

            return image

    @staticmethod
    def write(image, path=None):
        ''' Write PPM image to path '''
        if path is None:
            file = sys.stdout
        else:
            file = open(path, 'w')

        try:
            file.write('{}\n'.format(image.magic))
        except AttributeError:
            file.write('{}\n'.format(PPM.MAGIC))

        file.write('# DrawIt\n')
        file.write('{} {}\n'.format(image.width, image.height))

        try:
            file.write('{}\n'.format(image.max_value))
        except AttributeError:
            file.write('{}\n'.format(PPM.MAX_VALUE))

        for y in range(image.height):
            for x in range(image.width):
                color = image[Point(x, y)]
                file.write(bytearray([min(c, PPM.MAX_VALUE) for c in color.r, color.g, color.b]))

        file.close()

    @staticmethod
    def readline(stream):
        ''' Read in lines from stream, skipping lines that begin with # '''
        while True:
            line = stream.readline()
            if line[0] != '#':
                break

        return line.strip()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
