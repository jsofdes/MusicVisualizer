import random
import math
import pygame
class Flower(object):
    def __init__(self):
        self.color = [0, 0, 255]
        self.startangles = []
        self.endangles = []
        self.time = []
                self.radius_x = []
                self.radius_y = []
    def changeColor(self):
        y = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        return y

    def getAngles(self, x):
        # this is hard coded for simplicity. One can easily see how this can be
        # made into a for loop with something being appended to an array
        if x == 60:
            # self.startangles=[0, 60, 120, 180, 240, 300, 330]
            # self.endangles=[60, 120, 180, 240, 300, 330, 360]
            self.startangles = [-60, 0, 60, 120, 140, 200]
            self.endangles = [-60+180, 0+180, 60+180, 120+180, 140+180, 200+180]
        if x == 45:
            self.startangles = [-45, 0, 45, 90, 135, 180, 225, 270]
            self.endangles = [-45+180, 0+180, 45+180, 90+180, 135+180, 180+180, 225+180, 270+180]
        if x == 30:
            self.startangles = [-30, 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
            self.endangles = [-30+180, 0+180, 30+180, 60+180, 90+180, 120+180, 150+180, 180+180, 210+180, 240+180, 270+180, 300+180]

    def getCenter(self, x):
        rad_petal = 20
        petals = 360/x
        for i in range(0, x):
            self.radius_x.append(rad_petal*math.sin((x/2)+(2*x/2)))
            self.radius_y.append(rad_petal*math.cos((x/2)+(2*x/2)))

    def drawFlower(self, x, surfscreen):
        surface = pygame.Surface((100, 100))
        rectangle_wh = 100
        pygame.draw.arc(surface, self.color, (0, 0, 100, 100), -x/2, x/2)
        print("drewarc")
        rot_arc = pygame.transform.rotate(surface, x/2)
        y=rot_surface.get_rect().center = radius_x(i), radius_y(i)
        pygame.blit(y,surfscreen)
        print("draw screen")
        # if time == self.time(i):
        #     number_petals = i % (360/x)
        #     pygame.draw.circle[]
        # return s
