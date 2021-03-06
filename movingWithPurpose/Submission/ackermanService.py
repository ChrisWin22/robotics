import pygame
import math

class AckermanService:

    def __init__(self):
        super().__init__()

    def distance(self, cur_state, goal_state):
        return math.sqrt((goal_state[0] - cur_state[0])**2 + (goal_state[1] - cur_state[1])**2)

    def turn(self, angle, ackerman):
        dt = .1

        newLocal = [None,None,None]

        thetaDot = math.radians((ackerman.velocity/ackerman.length) * math.tan(angle) * dt)
        newLocal[2] = ackerman.facingDirection + thetaDot

        xDot = math.sin(newLocal[2]) * dt * ackerman.velocity 
        yDot = math.cos(newLocal[2]) * dt * ackerman.velocity

        newLocal[0] = ackerman.currentLocation[0] + xDot
        newLocal[1] = ackerman.currentLocation[1] + yDot


        return newLocal

    def getNewLocal(self, ackerman, endLocal):
        turningOptions = [-math.pi/4, -math.pi/8, 0, math.pi/8, math.pi/4]
        bestLocal = [None,None,None]
        bestTurn = 0
        bestDistance = 1000000000        

        for turn in turningOptions:
            newLocal = self.turn(turn, ackerman)
            newDistance = self.distance(newLocal, endLocal)
            if newDistance < bestDistance:
                bestDistance = newDistance
                bestLocal = newLocal
                bestTurn = turn
        print(bestTurn)
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
        pygame.draw.circle(surface, ackerman.color, [ackerman.currentLocation[0], ackerman.currentLocation[1]], 5, 0)

    def move(self, ackerman, endLocal):
        ackerman.currentLocation = self.getNewLocal(ackerman, endLocal)
        ackerman.facingDirection = ackerman.currentLocation[2]
        print(ackerman.currentLocation)






