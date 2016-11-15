''' image_tests.py: DrawIt image tests '''

import math
import unittest

from drawit.image import Image, Point, Color

# Image Unit Test

class ImageTest(unittest.TestCase):

    def test00_ImageInit(self):
        image = Image()
        self.assertTrue(image.width == Image.DEFAULT_WIDTH and image.height == Image.DEFAULT_HEIGHT)
        self.assertTrue(len(image.pixels) == Image.DEFAULT_HEIGHT)
        self.assertTrue(len(image.pixels[0]) == Image.DEFAULT_WIDTH)

        image = Image(32, 24)
        self.assertTrue(image.width == 32 and image.height == 24)
        self.assertTrue(len(image.pixels) == 24)
        self.assertTrue(len(image.pixels[0]) == 32)

        image = Image(height=32, width=24)
        self.assertTrue(image.width == 24 and image.height == 32)
        self.assertTrue(len(image.pixels) == 32)
        self.assertTrue(len(image.pixels[0]) == 24)

    def test01_ImageEq(self):
        image0 = Image()
        image1 = Image()
        self.assertTrue(image0 == image1)

        image0 = Image(32, 24)
        image1 = Image(height=24, width=32)
        self.assertTrue(image0 == image1)

    def test02_ImageStr(self):
        image = Image()
        self.assertTrue(str(image) == 'Image(width={},height={})'.format(Image.DEFAULT_WIDTH, Image.DEFAULT_HEIGHT))

        image = Image(32, 24)
        self.assertTrue(str(image) == 'Image(width=32,height=24)')

        image = Image(height=32, width=24)
        self.assertTrue(str(image) == 'Image(width=24,height=32)')

    def test03_ImageGetItem(self):
        image = Image()

        with self.assertRaises(IndexError):
            image[Point(-1, -1)]

        with self.assertRaises(IndexError):
            image[Point(0, image.height)]

        with self.assertRaises(IndexError):
            image[Point(image.width, 0)]

    def test03_ImageSetItem(self):
        image = Image()
        point = Point(0, 0)
        color = Color
        image[point] = color
        self.assertTrue(color == image[point])

    def test04_ImageClear(self):
        image = Image()
        color = Color()
        image.clear()

        for y in range(image.height):
            for x in range(image.width):
                self.assertTrue(image[Point(x, y)] == color)

    def test05_ImageLine(self):
        color  = Color(255, 0, 0)
        image  = Image()
        point0 = Point(0, 0)
        point1 = Point(10, 10)
        image.draw_line(point0, point1, color)
        for c in range(point1.y - point0.y):
            self.assertTrue(image[Point(c, c)] == color)
        
        image  = Image()
        point0 = Point(0, 0)
        point1 = Point(0, 10)
        image.draw_line(point0, point1, color)
        for y in range(point1.y - point0.y):
            self.assertTrue(image[Point(0, y)] == color)
        
        image  = Image()
        point0 = Point(0, 0)
        point1 = Point(10, 0)
        image.draw_line(point0, point1, color)
        for x in range(point1.x - point0.x):
            self.assertTrue(image[Point(x, 0)] == color)

    def test06_ImageRectangle(self):
        color  = Color(255, 0, 0)
        image  = Image()
        point0 = Point(0, 0)
        point1 = Point(10, 10)
        image.draw_rectangle(point0, point1, color)
        for y in range(point1.y - point0.y):
            for x in range(point1.x - point0.x):
                self.assertTrue(image[Point(x, y)] == color)
        
        image0 = Image()
        image1 = Image()
        image0.draw_rectangle(point0, point1, color)
        image1.draw_rectangle(point1, point0, color)
        self.assertTrue(image0 == image1)
    
    def test07_ImageCircle(self):
        color  = Color(255, 0, 0)
        image  = Image()
        center = Point(image.width / 2, image.height / 2)
        radius = 10

        image.draw_circle(center, radius, color)
        for y in range(image.height):
            for x in range(image.width):
                point = Point(x, y)
                if math.hypot(point.x - center.x, point.y - center.y) <= radius:
                    self.assertTrue(image[point] == color)

# Main execution

if __name__ == '__main__':
    unittest.main()
