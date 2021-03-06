from models.map import Map
import pygame
import math

class Rink(Map):
    SCALAR = 10
    OFFSET = 5

    def __init__(self, x=197, y=98.4, left=75, top = 75, radius = 28):
        super().__init__()
        self.rink_x = x
        self.rink_y = y
        self.left = left
        self.top = top
        self.radius = radius
        self.rink = pygame.Rect(left, top, self.rink_x * self.SCALAR, self.rink_y * self.SCALAR)
        self.rinkBorder = pygame.Rect(left-5, top-5, self.rink_x * self.SCALAR + 10, self.rink_y * self.SCALAR + 10)
    
    def get_scaled_x(self):
        return self.rink_x * self.SCALAR
    
    def get_scaled_y(self):
        return self.rink_y * self.SCALAR
    
    def is_inside(self, x, y):
        bottom = self.top + self.rink_y * self.SCALAR
        right = self.left + self.rink_x * self.SCALAR

        true_radius = self.radius*self.SCALAR

        if x > self.left and x < (right) and y > self.top and y < (bottom):
            if x > self.left + true_radius:
                #check top left
                if y > self.top + true_radius:
                    if not is_in_circle([x,y], [self.left+true_radius, self.top+true_radius],true_radius):
                        return False
                #check bottom left
                if y < bottom - true_radius:
                    if not is_in_circle([x,y], [self.left+true_radius, bottom+true_radius],true_radius):
                        return False
            if x < right - true_radius:
                #check top right
                if y > self.top + true_radius:
                    if not is_in_circle([x,y], [right+true_radius, self.top+true_radius],true_radius):
                        return False
                # check bottom right
                if y < bottom - true_radius:
                    if not is_in_circle([x,y], [right+true_radius, self.top+true_radius],true_radius):
                        return False
            return True
        return False

    def isInsideRink(self, x, y, off=0):
        _top = self.top + off
        _bottom = self.top + self.get_scaled_y() - off
        _left = self.left + off
        _right = self.left + self.get_scaled_x() - off
        r = self.radius * self.SCALAR - off

        #Make sure in full rectangle
        if x < _left or x > _right:
            return False
        if y < _top or y > _bottom:
            return False

        #Check if in inner rectangle
        if x > _left + r and x < _right - r:
            return True

        #Check if in second innner rectangle
        if y > _top + r and y < _bottom - r:
            return True
        
        #Check if in top left
        center = [_left + r, _top + r]
        if isInCircle(x, y, center, r):
            return True

        #Check if in top right
        center = [_right - r, _top + r]
        if isInCircle(x, y, center, r):
            return True

        #Check if in bottom left
        center = [_left + r, _bottom - r]
        if isInCircle(x,y,center,r):
            return True

        #Check if in bottom right
        center = [_right - r, _bottom - r]
        if isInCircle(x, y, center, r):
            return True

        #Not in rink
        return False


    
def isInCircle(x, y, center, radius):
    distance = math.sqrt((x - center[0]) ** 2 + (y - center[1]) **2) 
    if distance < radius:
        return True
    return False



def is_in_circle(g1,g2,radius):
    distance = math.sqrt((g1[0]-g2[0]) ** 2 + (g1[1]-g2[1]) ** 2 )
    if distance < radius:
        return True
    else:
        return False