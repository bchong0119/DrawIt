''' point.py: DrawIt Point '''

import math

class Point(object):

    def __init__(self, x=0, y=0):
        ''' Initialize Point object's instance variables '''
        self.x=int(x)
        self.y=int(y)


    def __eq__(self, other):
        ''' Returns True if current instance and other object are equal '''
        # TODO:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
       

    def __str__(self):
        ''' Returns string representing Point object '''
        # TODO:
        return "Point(x="+ str(self.x) +",y="+ str(self.y) +")"

    def distance_from(self, other):
        ''' Returns distance from current instance to other Point '''
        # TODO:
        d = math.hypot(self.x - other.x, self.y - other.y)
        return d



# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
