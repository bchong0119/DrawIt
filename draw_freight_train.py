#!/usr/bin/env python

from drawit import Image, Color, Point, PPM, WHITE, BLACK, RED

import math
import random

# Freight Train Colors

BLUE    = Color(30, 144, 255)
BROWN   = Color(129, 69, 19)
GRAY    = Color(180, 180, 180)
GREEN   = Color(154, 205, 50)
ORANGE  = Color(255, 165, 0)
PURPLE  = Color(72, 61, 139)
YELLOW  = Color(255, 215, 0)
SKYLINE = Color(248, 248, 248)

# Freight Train Image Class

class FreightTrain(Image):

    def draw_background(self):
        self.draw_rectangle(Point(0, 0), Point(self.width - 1, self.height - 1), WHITE)

    def draw_track(self):
        track_row = self.height * 7 / 8

        # Draw black tracks
        point0 = Point(0, track_row)
        point1 = Point(self.width - 1, track_row)
        self.draw_rectangle(point0, point1, BLACK)

        point0 = Point(0, track_row + 2)
        point1 = Point(self.width - 1, track_row + 2)
        self.draw_rectangle(point0, point1, BLACK)

        # Draw wooden blocks
        for column in range(0, self.width, 8):
            point0 = Point(column, track_row + 2)
            point1 = Point(column + 4, track_row + 6)
            self.draw_rectangle(point0, point1, BROWN)

    def draw_dirt(self):
        track_row = self.height * 7 / 8
        chance    = 1

        # Draw dirt such that the further away we get, the lower the chance of
        # drawing dirt
        for y in range(track_row + 6, self.height):
            for x in range(0, self.width):
                point = Point(x, y)
                if random.randint(0, 256) % chance == 0:
                    self[point] = BLACK
            chance += 1

    def draw_skyline(self):
        track_row      = self.height * 7 / 8
        car_height     = self.height / 20
        skyline_width  = self.width / 20
        skyline_height = self.height / 4
        x              = 0

        # Draw buildings of varying widths and heights
        while x < self.width:
            width  = skyline_width + random.randint(0, skyline_width / 2)
            height = skyline_height + random.randint(0, skyline_height / 2)
            point0 = Point(x, track_row - car_height*4)
            point1 = Point(point0.x + width - 2, point0.y - height)

            try:
                self.draw_rectangle(point0, point1, SKYLINE)
            except IndexError:
                pass
            x += width

    def draw_sun(self):
        sun_radius = self.width/40
        center     = Point(self.width - sun_radius*4, sun_radius*4)

        self.draw_circle(center, sun_radius*5/4, YELLOW)
        self.draw_circle(center, sun_radius, ORANGE)

    def draw_train_cars(self):
        track_row   = self.height * 7 / 8
        car_height  = self.height / 20
        car_width   = self.width / 10
        car_spacing = car_width + 2

        # Draw blue train car
        center = Point(self.width/2, track_row - car_height*3/2)
        self.draw_train_car(center, BLUE)

        # Draw purple train car
        center = Point(self.width/2 + car_spacing, track_row - car_height*3/2)
        self.draw_train_car(center, PURPLE)

        # Draw black train car
        center = Point(self.width/2 + car_spacing*2, track_row - car_height*3/2)
        self.draw_train_car(center, BLACK)

        # Draw green train car
        center = Point(self.width/2 - car_spacing, track_row - car_height*3/2)
        self.draw_train_car(center, GREEN)

        # Draw yellow train car
        center = Point(self.width/2 - car_spacing*2, track_row - car_height*3/2)
        self.draw_train_car(center, YELLOW)

        # Draw orange train car
        center = Point(self.width/2 - car_spacing*3, track_row - car_height*3/2)
        self.draw_train_car(center, ORANGE)

        # Draw red train car
        center = Point(self.width/2 - car_spacing*4, track_row - car_height*3/2)
        self.draw_train_car(center, RED)

    def draw_train_car(self, center, color):
        car_width  = self.width / 10
        car_height = self.height / 20

        # Draw body
        point0 = Point(center.x - car_width/2, center.y - car_height/2)
        point1 = Point(center.x + car_width/2, center.y + car_height/2)
        self.draw_rectangle(point0, point1, color)

        # Draw wheels
        point0 = Point(center.x - car_width/4, center.y + car_height)
        self.draw_circle(point0, car_width/8, BLACK)
        point0 = Point(center.x + car_width/4, center.y + car_height)
        self.draw_circle(point0, car_width/8, BLACK)

    def draw_train_engine(self):
        track_row   = self.height * 7 / 8
        car_height  = self.height / 20
        car_width   = self.width / 10
        car_spacing = car_width + 2
        center      = Point(self.width/2 + car_spacing*3, track_row - car_height*1.5)

        # Draw engine body
        self.draw_train_car(center, BLACK)
        self.draw_train_car(Point(center.x + car_width / 4, center.y), BLACK)

        # Draw engine cockpit
        point0 = Point(center.x - car_width / 2, center.y + car_height / 2)
        point1 = Point(center.x + car_width / 8, center.y - car_height*1.5)
        self.draw_rectangle(point0, point1, BLACK)
        point0 = Point(center.x - car_width*0.40, center.y - car_height*0.6)
        point1 = Point(center.x + car_width*0.05, center.y - car_height*1.35)
        self.draw_rectangle(point0, point1, WHITE)

        # Draw engine grill
        point0 = Point(center.x + car_width*0.65, center.y + car_height*0.5)
        point1 = Point(center.x + car_width*1.00, center.y + car_height*1.3)
        self.draw_rectangle(point0, point1, BLACK)

        # Draw engine smokestack
        point0 = Point(center.x + car_width*0.45, center.y - car_height*0.5)
        point1 = Point(center.x + car_width*0.55, center.y - car_height*0.7)
        self.draw_rectangle(point0, point1, BLACK)
        point0 = Point(center.x + car_width*0.40, center.y - car_height*0.7)
        point1 = Point(center.x + car_width*0.60, center.y - car_height*0.9)
        self.draw_rectangle(point0, point1, BLACK)
        point0 = Point(center.x + car_width*0.35, center.y - car_height*0.9)
        point1 = Point(center.x + car_width*0.65, center.y - car_height*1.1)
        self.draw_rectangle(point0, point1, BLACK)
        point0 = Point(center.x + car_width*0.30, center.y - car_height*1.1)
        point1 = Point(center.x + car_width*0.70, center.y - car_height*1.5)
        self.draw_rectangle(point0, point1, BLACK)

    def draw_train_smoke(self):
        car_height  = self.height / 20
        car_width   = self.width / 10
        car_spacing = car_width + 2
        track_row   = self.height * 7 / 8
        radius      = car_width / 32
        center      = Point(self.width/2 + car_spacing*3, track_row - car_height*1.5)
        point       = Point(center.x + car_width*0.5, center.y - car_height*1.75)
        color       = Color(GRAY.r, GRAY.g, GRAY.b)
        dx          = 0

        while radius < car_width:
            self.draw_circle(point, radius, color)

            dx      += 1
            point.x -= int(dx*car_width*0.5)
            point.y -= int(math.log(car_width*0.5*dx)*car_height*0.5)
            radius  += radius
            color.r += 12
            color.g += 12
            color.b += 12

# Main Execution

if __name__ == '__main__':
    # Draw Freight Train Scene
    freight_train = FreightTrain()
    freight_train.draw_background()
    freight_train.draw_track()
    freight_train.draw_dirt()
    freight_train.draw_skyline()
    freight_train.draw_sun()
    freight_train.draw_train_cars()
    freight_train.draw_train_engine()
    freight_train.draw_train_smoke()

    # Write image to stdout
    PPM.write(freight_train)

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
