import random
import math
import pygame
class Flower(object):
    def __init__(self):
        self.color = [255, 0, 0]
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
        for i in range(0, petals):
            self.radius_x.append((rad_petal*math.sin(math.radians((x/2)+(2*i*x/2)))))
            self.radius_y.append((rad_petal*math.cos(math.radians((x/2)+(2*i*x/2)))))
        print("radx, y", self.radius_x,self.radius_y)

    def drawFlower(self, x, surfscreen):
        surface = pygame.Surface((100, 100))
        surface.set_alpha(100)
        rectangle_wh = 100
        pygame.draw.arc(surface, self.color, (0, 0, 100, 100), math.radians(-x/2), math.radians(x/2), 5)
        print("drewarc")
        print(x)
        rot_arc = pygame.transform.rotate(surface, x/2)
        petals = 360/x
        for i in range(0, petals):
            print(i)
            rot_arc.get_rect().center = (self.radius_x[i], self.radius_y[i])
            surfscreen.blit(rot_arc, (self.radius_x[i], self.radius_y[i]))
        print("draw screen")
        # if time == self.time(i):
        #     number_petals = i % (360/x)
        #     pygame.draw.circle[]
        # return s
