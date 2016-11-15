#! /usr/bin/env python

from drawit import Image, Color, Point, PPM

import math

# Colors to use

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
GREY = Color(180, 180, 180)
DARKGREY = Color(160, 160, 160)
DARKBLUE = Color(0, 55, 110)
BLUEGREY = Color(20, 25, 50)
PURPLE = Color(233, 24, 255)
CYAN = Color(102, 255, 255)



# my images

class bchong(Image):

    def draw_halfcircle(self, center, radius, color):
	#bottom half
	if radius==0:
	    self.pixels[center.y][center.x]=color
	else:
	    #for in rectangle that bounds half circle, if point in circle, color
	    for x in range(center.x-radius-1, center.x+radius+1):
	        for y in range(center.y, center.y+radius+1):
		    #if distance from center <=radius, color
		    point = Point(x, y)
		    if point.distance_from(center) <= radius:
		    	self.pixels[y][x]=color

    def draw_background(self):
    	self.draw_rectangle(Point(0, 0), Point(self.width-1, self.height-1), DARKBLUE)
	self.draw_rectangle(Point(0, (self.height/2)-30), Point(self.width-1, self.height-1), BLUEGREY)
	self.draw_rectangle(Point(0, (self.height/2)-10), Point(self.width-1, (self.height/2)-1), PURPLE)
	self.draw_rectangle(Point(0, self.height-30), Point(self.width-1, self.height-20), PURPLE)
	self.draw_rectangle(Point(0, 325), Point(self.width-1, 365), CYAN)

    def draw_pokeball(self):
        #center of image
        center = Point(self.width/2, self.height/2)

        #red half
	self.draw_circle(center, 100, RED)

	#white half
	self.draw_halfcircle(center, 100, WHITE)

	#black line in middle and black circle in middle
	self.draw_rectangle(Point(center.x-100, center.y-8), Point(center.x+100, center.y+8), BLACK)
	self.draw_circle(center, 30, BLACK)

	#button in middle
	self.draw_circle(center, 19, GREY)
	self.draw_circle(center, 15, DARKGREY)
	self.draw_circle(center, 13, GREY)

	#reflection
	self.draw_circle(Point(center.x+45, center.y-60), 16, WHITE)
	self.draw_circle(Point(center.x+70, center.y-35), 8, WHITE)


# Main Execution

if __name__ == '__main__':
    # Draw everything
    mine = bchong()
    mine.draw_background();
    mine.draw_pokeball();

    #write image to stdout
    PPM.write(mine)

