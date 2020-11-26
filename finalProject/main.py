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
        time.sleep(3)
        return True
    return False

def enterRink(ackerman, rink, rink_service, screen, presets, ackermanService):
    entranceLocal = presets.dock 
    while True:
        screen.fill((0,0,0))
        rink_service.draw_dock(rink,presets.dock[0],presets.dock[1])
        rink_service.drawRink(rink)
        ackermanService.move(ackerman, entranceLocal)
        ackermanService.draw(screen, ackerman)
        pygame.display.update()
        if checkArrived(ackerman, entranceLocal):
            return



def main():
    pygame.init()

    rink_service = RinkService()
    importService = ImportService()
    importService.setFile("config_assignment3.json")
    presets = importService.getPresets()

    endLocal = presets.endLocation
    startLocal = presets.startLocation
    #startLocal = [75,75]

    ackerman = Ackerman(currentLocation=startLocal, maxSteeringAngle=math.radians(presets.maxSteeringAngle), facingDirection=presets.facingDirection,velocity=3)
    ackermanService = AckermanService()

    keepRunning = True
    mapping = rink_service.determine_rink(presets.name)
    screen = mapping.display

    enterRink(ackerman, mapping, rink_service, screen, presets, ackermanService)

    while keepRunning:
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


if __name__ == "__main__":
    main()
