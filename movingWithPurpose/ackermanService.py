import pygame
import math

class AckermanService:

    def __init__(self):
        super().__init__()

    def draw(self, surface, ackerman):
        pygame.draw.circle(surface, ackerman.color, [ackerman.currentLocation[0], ackerman.currentLocation[1]], 5, 0)

    def move(self, ackerman, endLocal):
        print("Current Location: " , ackerman.currentLocation)
        dt = .5
        alpha = self.getAlpha(ackerman, endLocal)
        ackerman.currentLocation[0] += math.sin(alpha) * dt * ackerman.velocity 
        ackerman.currentLocation[1] += -1 * math.cos(alpha) * dt * ackerman.velocity
        ackerman.facingDirection += (ackerman.velocity/ackerman.length) * math.tan(alpha) * dt
        print("New Location: " , ackerman.currentLocation)



    def getAlpha(self, ackerman, endLocal):
        angleToGoal = math.atan((endLocal[1] - ackerman.currentLocation[1])/(endLocal[0] - ackerman.currentLocation[0]))
        if angleToGoal == ackerman.facingDirection:
            return 0
        alpha = min(ackerman.maxSteeringAngle, abs(angleToGoal))
        if angleToGoal < 0:
            alpha *= -1
        return alpha



