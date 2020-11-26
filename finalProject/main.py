from help.movingDot import MovingDot
from services.importService import ImportService
from help.movingDotService import MovingDotService
import time
from models.presets import Presets
import pygame
from models.ackerman import Ackerman
from services.ackermanService import AckermanService
from services.rinkService import RinkService
import math

def checkArrived(ackerman, dot, endLocal):
    global keepRunning

    tempX = endLocal[0] - ackerman.currentLocation[0]
    tempY = endLocal[1] - ackerman.currentLocation[1]
    if (tempX < 1 and tempX > -1) and (tempY < 1 and tempY > -1):
        time.sleep(3)
        keepRunning = False

def main():
    pygame.init()

    rink_service = RinkService()
    importService = ImportService()
    importService.setFile("config_assignment3.json")
    presets = importService.getPresets()

    endLocal = presets.endLocation
    startLocal = presets.startLocation
    #startLocal = [75,75]

    dot = MovingDot(currentLocation=startLocal)
    dotService = MovingDotService()

    ackerman = Ackerman(currentLocation=startLocal, maxSteeringAngle=math.radians(presets.maxSteeringAngle), facingDirection=presets.facingDirection,velocity=5)
    ackermanService = AckermanService()

    keepRunning = True
    mapping = rink_service.determine_rink(presets.name)
    screen = mapping.display

    

    while keepRunning:
        screen.fill((0,0,0))
        rink_service.draw_dock(mapping,presets.dock[0],presets.dock[1])
        rink_service.drawRink(mapping)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepRunning = False
                break
        # ackermanService.move(ackerman, endLocal)
        # ackermanService.draw(screen, ackerman)
        pygame.display.update()
        # checkArrived(ackerman, dot, endLocal)
        # time.sleep(.05)
    pygame.quit()


if __name__ == "__main__":
    main()
