import math
import pygame

class Ackerman:

    def __init__(self, img, currentLocation = [0,0], velocity=0, color=[255,0,0], facingDirection = 0, maxSteeringAngle = 0, length = 1):
        self.color = color
        self.currentLocation = currentLocation
        self.velocity = velocity
        self.facingDirection = facingDirection
        self.length = length
        self.maxSteeringAngle = maxSteeringAngle
        self.currentLocation[2] = math.radians(self.currentLocation[2])
        self.img = img
        self.visited = []
        self.pathIncrement = 0
        self.pathColor = [77,238,234,10]
#        self.rectangle = pygame.Rect(0,0,0,0)
#        self.rectangle.width = width
#        self.rectangle.height = length
#        self.rectangle.center = (currentLocation[0], currentLocation[1])
        super().__init__()