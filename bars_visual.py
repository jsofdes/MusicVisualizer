import random
import math
import pygame
from random import randint
import random
class Bar(object):
    def __init__(self):
        self.color = [255, 0, 0]
        self.startangles = []
        self.endangles = []
        self.time = []
        self.radius_x = []
        self.radius_y = []
        self.song_anal = []
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
        petals = x
        for i in range(0, int(petals)):
            self.radius_x.append((rad_petal*math.sin(math.radians((x/2)+(2*i*x/2)))))
            self.radius_y.append((rad_petal*math.cos(math.radians((x/2)+(2*i*x/2)))))




    def drawBar(self, x, surfscreen):
        petals = x
        random_tempo = random.shuffle(self.song_anal)
        for i in self.song_anal:
            color_count = i
            surface = pygame.Surface((i , i ))
            surface.set_alpha(100+ i)
            rectangle_wh = 100 + i
            pygame.draw.arc(surface, [randint(0,255), randint(0,255), randint(0,255)], (0, 0, 100, 100), math.radians(-x/2)-i, math.radians(x/2)-i, 5)
            rot_arc = pygame.transform.rotate(surface, i/2)
            rot_arc.get_rect().center = (i, i)
            print(color_count)
            surfscreen.blit(rot_arc, (randint(0,800),randint(0,600)))
            pygame.display.update()
            pygame.time.delay(200)
