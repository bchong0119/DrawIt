''' color.py: DrawIt Color '''

class Color(object):
    def __init__(self, r=0, g=0, b=0):
        ''' Initialize Color object's instance variables '''
        self.r=r
	self.g=g
	self.b=b

    def __eq__(self, other):
        ''' Returns True if current instance and other object are equal '''
        if self.r==other.r and self.g==other.g and self.b==other.b:
	    return self.r==other.r and self.g==other.g and self.b==other.b

    def __str__(self):
        ''' Returns string representing Color object '''
	return 'Color(r={},g={},b={})'.format(self.r, self.g, self.b)  


# TODO: Define basic colors
WHITE   = Color(255, 255, 255)
RED     = Color(255, 0, 0)
GREEN   = Color(0, 255, 0)
BLUE    = Color(0, 0, 255)
CYAN    = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW  = Color(255, 255, 0)
BLACK   = Color(0, 0, 0)

# TODO: Define list of basic colors
COLORS  = [
    WHITE, RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, BLACK
]

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
