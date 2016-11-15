#! /usr/bin/env python

from drawit import Image, Color, Point, PPM

import math
import random

# snowman colors 
WHITE    = Color(255, 255, 255)
BLACK    = Color(0, 0, 0)
ORANGE   = Color(255, 165, 0)
SKYBLUE  = Color(204, 255, 255)
GREY     = Color(180, 180, 180)

class SnowMan(Image):

    def draw_background(self):
        self.draw_rectangle(Point(0, 0), Point(self.width-1, self.height-1), SKYBLUE)

    def draw_snow(self):
    	self.draw_rectangle(Point(0, 380), Point(self.width-1, self.height-1), GREY)

    def draw_snowman(self):
        #big bottom circle
        self.draw_circle(Point(400, 380), 80, WHITE)

	#small top circle
	self.draw_circle(Point(400, 280), 40, WHITE)

	#hat
	self.draw_rectangle(Point(350, 240), Point(450, 260), BLACK)
	self.draw_rectangle(Point(365, 170), Point(435, 240), BLACK)

	#face
	#eyes
	self.draw_circle(Point(385, 270), 5, BLACK)
	self.draw_circle(Point(415, 270), 5, BLACK)

	#nose
	self.draw_circle(Point(400, 280), 7, ORANGE)

	#mouth
	self.draw_rectangle(Point(380, 295), Point(420, 300), BLACK)

	#draw buttons
	self.draw_circle(Point(400, 380), 10, BLACK)
	self.draw_circle(Point(400, 340), 10, BLACK)



if __name__ == '__main__':
    #draw snowman
    snowman=SnowMan()
    snowman.draw_background()
    snowman.draw_snow()
    snowman.draw_snowman()

    #Write image to stdout
    PPM.write(snowman)
