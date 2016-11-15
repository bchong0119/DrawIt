''' point_tests.py: DrawIt point tests '''

import math
import unittest

import drawit.point

# Point Unit Test

class PointTest(unittest.TestCase):

    def test00_PointInit(self):
        point = drawit.point.Point()
        self.assertTrue(point.x == 0 and point.y == 0)

        point = drawit.point.Point(1, 2)
        self.assertTrue(point.x == 1 and point.y == 2)

        point = drawit.point.Point(y=1, x=2)
        self.assertTrue(point.x == 2 and point.y == 1)
    
    def test01_PointStr(self):
        point0 = drawit.point.Point()
        point1 = drawit.point.Point()
        self.assertTrue(point0 == point1)
        
        point0 = drawit.point.Point(1, 2)
        point1 = drawit.point.Point(y=2, x=1)
        self.assertTrue(point0 == point1)

    def test02_PointStr(self):
        point = drawit.point.Point()
        self.assertTrue(str(point) == 'Point(x=0,y=0)')

        point = drawit.point.Point(1, 2)
        self.assertTrue(str(point) == 'Point(x=1,y=2)')

        point = drawit.point.Point(y=1, x=2)
        self.assertTrue(str(point) == 'Point(x=2,y=1)')

    def test03_PointDistanceFrom(self):
        point0 = drawit.point.Point(0, 0)
        point1 = drawit.point.Point(1, 1)
        self.assertTrue(point0.distance_from(point1) == 1.4142135623730951)

        point0 = drawit.point.Point(1, 2)
        point1 = drawit.point.Point(2, 1)
        self.assertTrue(point0.distance_from(point1) == 1.4142135623730951)

# Main Execution

if __name__ == '__main__':
    unittest.main()
