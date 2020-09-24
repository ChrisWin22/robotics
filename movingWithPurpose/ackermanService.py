import pygame
import math

class AckermanService:

    def __init__(self):
        super().__init__()

    def getAlpha(self, ackerman, endLocal):
        deltaY = (endLocal[1] - ackerman.currentLocation[1])
        deltaX = (endLocal[0] - ackerman.currentLocation[0])
        if deltaX == 0:
            angleToGoal = math.pi/2
        else:
            angleToGoal = math.atan(deltaY/deltaX)
        if angleToGoal == ackerman.facingDirection:
            return 0
        alpha = min(ackerman.maxSteeringAngle, abs(angleToGoal - ackerman.facingDirection))
        if angleToGoal - ackerman.facingDirection < 0:
            alpha *= -1
        return alpha

    def draw(self, surface, ackerman):
        pygame.draw.circle(surface, ackerman.color, [ackerman.currentLocation[0], ackerman.currentLocation[1]], 5, 0)

    def move(self, ackerman, endLocal):
        dt = .1

        #alpha = self.getAlpha(ackerman, endLocal)
        alpha = math.pi/4

        xDot = math.sin(ackerman.facingDirection) * dt * ackerman.velocity 
        yDot = math.cos(ackerman.facingDirection) * dt * ackerman.velocity
        thetaDot = math.radians((ackerman.velocity/ackerman.length) * math.tan(alpha) * dt)

        ackerman.currentLocation[0] = ackerman.currentLocation[0] + xDot
        ackerman.currentLocation[1] = ackerman.currentLocation[1] + yDot
        ackerman.facingDirection = ackerman.facingDirection + thetaDot

        ackerman.currentLocation[2] = math.degrees(ackerman.facingDirection)
        print("Location: " , ackerman.currentLocation)






