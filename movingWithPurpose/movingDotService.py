import pygame
import math

class MovingDotService:

    def __init__(self):
        super().__init__()

    
    def draw(self, surface, dot):
        pygame.draw.circle(surface, dot.color, [dot.currentLocation[0], dot.currentLocation[1]], 5, 0)

    def calcNewLocal(self, dot, endLocal):
        theta = abs(math.atan((endLocal[1] - dot.currentLocation[1])/(endLocal[0] - dot.currentLocation[0])))
        y = dot.currentVelocity * math.sin(theta)
        x = dot.currentVelocity * math.cos(theta)
        if endLocal[1] < dot.currentLocation[1]:
            y *= -1
        if endLocal[0] < dot.currentLocation[0]:
            x *= -1
        dot.currentLocation[0] += x
        dot.currentLocation[1] += y
        return [dot.currentLocation[0], dot.currentLocation[1]]

    def move(self, dot, endLocal):
        dot.currentLocation = self.calcNewLocal(dot, endLocal)

