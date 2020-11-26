from map import Map
import pygame

class Rink(Map):
    SCALAR = 10

    def __init__(self, x=197, y=98.4, left=75, top = 75, radius = 28):
        super().__init__()
        self.rink_x = x
        self.rink_y = y
        self.left = left
        self.top = top
        self.radius = radius
        self.rink = pygame.Rect(left, top, self.rink_x * self.SCALAR, self.rink_y * self.SCALAR)
    
    def get_scaled_x(self):
        return self.rink_x * self.SCALAR
    
    def get_scaled_y(self):
        return self.rink_y * self.SCALAR
    
    def is_inside(self, x, y):
        return True if x > self.left and x < (self.left + self.rink_x * self.SCALAR) and y > self.top and y < (self.top + self.rink_y * self.SCALAR) else False