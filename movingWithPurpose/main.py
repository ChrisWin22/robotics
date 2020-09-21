from movingDot import MovingDot
from importService import ImportService
from movingDotService import MovingDotService
import time
from presets import Presets
import pygame
from ackerman import Ackerman
from ackermanService import AckermanService

def checkArrived(ackerman, dot, endLocal):
    global keepRunning

    tempX = endLocal[0] - ackerman.currentLocation[0]
    tempY = endLocal[1] - ackerman.currentLocation[1]
    if (tempX < 1 and tempX > -1) and (tempY < 1 and tempY > -1):
        time.sleep(3)
        keepRunning = False


pygame.init()

importService = ImportService()
importService.setFile("config_assignment3.json")
presets = importService.getPresets()

endLocal = presets.endLocation
#startLocal = presets.startLocation
startLocal = [75,75]

dot = MovingDot(currentLocation=startLocal)
dotService = MovingDotService()

ackerman = Ackerman(currentLocation=startLocal, maxSteeringAngle=presets.maxSteeringAngle, facingDirection=presets.facingDirection,velocity=1)
ackermanService = AckermanService()

keepRunning = True
screen = pygame.display.set_mode((1000, 1000))

while keepRunning:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False
            break
    dotService.move(dot, endLocal)
    dotService.draw(screen, dot)
    ackermanService.move(ackerman, endLocal)
    ackermanService.draw(screen, ackerman)
    pygame.display.update()
    checkArrived(ackerman, dot, endLocal)
    time.sleep(.05)
pygame.quit()