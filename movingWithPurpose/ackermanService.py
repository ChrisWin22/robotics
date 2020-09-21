import pygame
import math

class AckermanService:

    def __init__(self):
        super().__init__()

    def draw(self, surface, ackerman):
        pygame.draw.circle(surface, ackerman.color, [ackerman.currentLocation[0], ackerman.currentLocation[1]], 5, 0)

    def move(self, ackerman, endLocal):
        needToTurnDegrees = math.atan((endLocal[0] - ackerman.currentLocation[0])/(endLocal[1] - ackerman.currentLocation[1]))#theta
        alpha = min(abs(needToTurnDegrees - ackerman.facingDirection), abs(needToTurnDegrees + (2 * math.pi) - ackerman.facingDirection), abs(needToTurnDegrees - (ackerman.facingDirection + 2 * math.pi)))
        alpha = needToTurnDegrees
        if alpha > 0.785398:
            alpha = 0.785398
        elif alpha < -0.785398:
            alpha = -0.785398
        thetaDot = ackerman.velocity * math.tan(alpha) #where I want my wheels facing
        ackerman.currentLocation[0] += (ackerman.velocity * math.sin(thetaDot)) * .5
        ackerman.currentLocation[1] += (-ackerman.velocity * math.cos(thetaDot)) * .5
        ackerman.facingDirection += thetaDot * .5
