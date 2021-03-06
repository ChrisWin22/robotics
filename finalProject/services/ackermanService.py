import pygame
import math
from models.rinks.rink import Rink

class AckermanService:

    def __init__(self):
        super().__init__()
        self.rink = Rink()

    def distance(self, cur_state, goal_state):
        return math.sqrt((goal_state[0] - cur_state[0])**2 + (goal_state[1] - cur_state[1])**2)

    def turn(self, angle, ackerman, dt=.01):

        newLocal = [None,None,None]

        thetaDot = math.radians((ackerman.velocity/ackerman.length) * math.tan(angle) * dt)
        newLocal[2] = ackerman.facingDirection + thetaDot

        xDot = math.sin(newLocal[2]) * dt * ackerman.velocity 
        yDot = math.cos(newLocal[2]) * dt * ackerman.velocity

        newLocal[0] = ackerman.currentLocation[0] + xDot
        newLocal[1] = ackerman.currentLocation[1] + yDot


        return newLocal

    def getNewLocal(self, ackerman, endLocal):
        turningOptions = [-math.pi/3,-math.pi/4, -math.pi/8, 0, math.pi/8, math.pi/4, math.pi/3]
        bestLocal = [None,None,None]
        bestTurn = 0
        bestDistance = 1000000000        

        for t in range(1000, 2, -1):
            degree = -math.pi/t
            newLocal = self.turn(degree, ackerman)
            newDistance = self.distance(newLocal, endLocal)
            if newDistance < bestDistance:
                bestDistance = newDistance
                bestLocal = newLocal
                bestTurn = degree
        
        newLocal = self.turn(0, ackerman)
        newDistance = self.distance(newLocal, endLocal)
        if newDistance < bestDistance:
            bestDistance = newDistance
            bestLocal = newLocal
            bestTurn = degree
        
        for t in range(8, 2, -1):
            degree = math.pi/t
            newLocal = self.turn(degree, ackerman)
            newDistance = self.distance(newLocal, endLocal)
            if newDistance < bestDistance:
                bestDistance = newDistance
                bestLocal = newLocal
                bestTurn = degree
        
        # for turn in turningOptions:
        #     newLocal = self.turn(turn, ackerman)
        #     newDistance = self.distance(newLocal, endLocal)
        #     if newDistance < bestDistance:
        #         bestDistance = newDistance
        #         bestLocal = newLocal
        #         bestTurn = turn
        # print(bestTurn)
        # bestLocal = self.turn(math.pi/4, ackerman)
        return bestLocal

    def getAlpha(self, ackerman, endLocal):
        deltaY = (endLocal[1] - ackerman.currentLocation[1])
        deltaX = (endLocal[0] - ackerman.currentLocation[0])
        if deltaX == 0:
            angleToGoal = math.pi/2
        else:
            angleToGoal = math.atan(deltaY/deltaX)
        deltaAlpha = abs(angleToGoal - ackerman.facingDirection)
        if deltaAlpha < .01:
            return 0
        alpha = min(ackerman.maxSteeringAngle, abs(angleToGoal - ackerman.facingDirection))
        if angleToGoal - ackerman.facingDirection < 0:
            alpha *= -1
        return alpha

    def draw(self, surface, ackerman):

        
        # loc = ackerman.img.get_rect().center 
        # rot_sprite = pygame.transform.rotate(ackerman.img, math.degrees(ackerman.facingDirection) + 90 )
        # rot_sprite.get_rect().center = loc
        # surface.blit(rot_sprite, (ackerman.currentLocation[0] - 40, ackerman.currentLocation[1]) )
        pygame.draw.circle(surface, ackerman.color, [ackerman.currentLocation[0], ackerman.currentLocation[1]], 5, 0)

    def move(self, ackerman, endLocal):
        ackerman.currentLocation = self.getNewLocal(ackerman, endLocal)
        ackerman.facingDirection = ackerman.currentLocation[2]
        # print(ackerman.currentLocation)

    def hasVisited(self, ackerman, x, y):
        for local in ackerman.visited:
            distance = math.sqrt((x - local[0]) ** 2 + (y - local[1]) ** 2)
            if distance < 10:
                return True
        return False


