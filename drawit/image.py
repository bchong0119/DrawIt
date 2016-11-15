''' image.py: DrawIt Image '''

from color import Color
from point import Point

import math
import numpy as np

class Image(object):
    DEFAULT_WIDTH  = 640
    DEFAULT_HEIGHT = 480

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        ''' Initialize Image object's instance variables '''
        # TODO
        self.width = width
        self.height = height
        self.pixels = []

        for row in range(self.height):
            pixelrow = []
            for column in range(self.width):
                pixelrow.append(Color())
	    self.pixels.append(pixelrow)

    def __eq__(self, other):
        ''' Returns True if current instance and other object are equal '''
        # TODO
        if self.width == other.width and self.height == other.height:
            return True
        else:
            return False

    def __str__(self):
        ''' Returns string representing Image object '''
        # TODO       
	return 'Image(width={},height={})'.format(self.width, self.height)

    def __getitem__(self, point):
        ''' Returns pixel color specified by point

        If point is not with the bounds of the Image, then an IndexError is raised.
        '''
        # TODO
    	if point.x>=0 and point.x<self.width and point.y>=0 and point.y<self.height:
            #print "("+point.x+","+point.y+")"
    	    return self.pixels[point.y][point.x]
        else:
            #print "("+str(point.x)+","+str(point.y)+")"
            raise IndexError


    def __setitem__(self, point, color):
        ''' Sets pixel specified by point to given color

        If point is not with the bounds of the Image, then an IndexError is raised.
        '''
        # TODO
        if point.x>=0 and point.x<self.width and point.y>=0 and point.y<self.height:
            self.pixels[int(point.y)][int(point.x)]=color 
	    #self.point.x==Color() and self.point.y==Color() 
        else:
            raise IndexError


    def clear(self):
        ''' Clears Image by setting all pixels to default Color '''
        # TODO
        self.pixels = []
        color = Color()

        for row in range(self.height):
            pixelrow = []
            for column in range(self.width):
                pixelrow.append(color)
            self.pixels.append(pixelrow)

    def draw_line(self, point0, point1, color):
        ''' Draw a line from point0 to point1 '''
        # TODO
	#check if point0 and point1 are same point or vertical
	if point0.x==point1.x:
	    if point0.y<=point1.y:
	        starty=point0.y
		endy=point1.y
	    else:
	        starty=point1.y
		endy=point0.y
    
	    for y in range(starty, endy+1):
	        self.pixels[y][point0.x]=color
        else: 
	    #calculate slope
	    m=(float(point1.y-point0.y))/(point1.x-point0.x)

	    #calculate y int
	    yint=point0.y-(m*point0.x)

	    #start with point with smaller x
	    if point0.x<=point1.x:
	        start=point0.x
	    else:
	        start=point1.x

	    #plot points and mark with color
	    for x in np.arange(start, abs(point1.x-point0.x)+start+0.025, 0.025):
	        y=(m*x)+yint
	        self.pixels[math.trunc(y)][math.trunc(x)]=color


    def draw_rectangle(self, point0, point1, color):
        ''' Draw a rectangle from point0(top left) to point1(bottom right) '''
        # TODO
        xmin=min(point0.x, point1.x)
        xmax=max(point0.x, point1.x)
        ymin=min(point0.y, point1.y)
        ymax=max(point0.y, point1.y)

        for column in range(xmin,xmax):
            for row in range(ymin,ymax):
                self[Point(column,row)]=color


    def draw_circle(self, center, radius, color):
        ''' Draw a filled in circle with center point and radius '''
        # TODO
	#if radius==0, just draw point
        if radius==0:
	    self.pixels[center.y][center.x]=color
	else:
	    #for in rectangle that bounds circle, if point is in circle, color
	    for x in range(center.x-radius-1, center.x+radius+1):
	        for y in range(center.y-radius-1, center.y+radius+1):
		    #if distance from center <= radius, color
		    point = Point(x, y)
		    if point.distance_from(center) <= radius:
		        self.pixels[y][x]=color
                
    def draw_square(self, point, length, color):
        xmin=min(point.x, length.x)
        xmax=max(point.x, length.x)
        ymin=min(point.y, length.y)
        ymax=max(point.y, length.y)

        for column in range(xmin, xmax):
            for row in range(ymin, ymax):
                self[Point(column,row)]=color


# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
