from services.importService import ImportService
import time
from models.presets import Presets
import pygame
from models.ackerman import Ackerman
from services.ackermanService import AckermanService
from services.rinkService import RinkService
import math
from models.rinks import rink


def checkArrived(ackerman, endLocal):
    tempX = endLocal[0] - ackerman.currentLocation[0]
    tempY = endLocal[1] - ackerman.currentLocation[1]
    if (tempX < 1 and tempX > -1) and (tempY < 1 and tempY > -1):
        return True
    return False


def moveAckerman(moveTo):
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepRunning = False
                break
        rink_service.draw_dock(mapping,presets.dock[0],presets.dock[1])
        rink_service.drawRink(mapping)
        ackermanService.move(ackerman, moveTo)
        ackermanService.draw(screen, ackerman)
        pygame.display.update()
        if checkArrived(ackerman, moveTo):
            return

def enterRink():
    entranceLocal = presets.dock[0], presets.dock[1]
    moveAckerman(entranceLocal)
    rinkOpening = presets.dock[0] + (4.7*mapping.SCALAR), presets.dock[1] + (2.3*mapping.SCALAR)/2
    moveAckerman(rinkOpening)


def main():
    pygame.init()

    enterRink()

    while True:
        screen.fill((0,0,0))
        rink_service.draw_dock(mapping,presets.dock[0],presets.dock[1])
        rink_service.drawRink(mapping)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepRunning = False
                break
        # ackermanService.move(ackerman, endLocal)
        ackermanService.draw(screen, ackerman)
        pygame.display.update()
        # checkArrived(ackerman, endLocal)
        # time.sleep(.05)
    pygame.quit()

#Needed Global Variables
rink_service = RinkService()
importService = ImportService()
importService.setFile("config_assignment3.json")
presets = importService.getPresets()
startLocal = presets.startLocation
ackerman = Ackerman(currentLocation=startLocal, maxSteeringAngle=math.radians(presets.maxSteeringAngle), facingDirection=presets.facingDirection,velocity=1, length=.8)
ackermanService = AckermanService()
mapping = rink_service.determine_rink(presets.name)
screen = mapping.display
if __name__ == "__main__":
    main()
