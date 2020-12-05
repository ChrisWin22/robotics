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

def drawPointAtLocal(local):
    pygame.draw.circle(screen, [0,255,0], [local[0],local[1]], 5, 0)
    pygame.display.update()



def firstLap():
    turningOptions = [0, 1]
    moveDistance = 10
    while True:
        for o in turningOptions:
            if o == 0:
                nextLocation = ackermanService.turn(o,ackerman, moveDistance)
                drawPointAtLocal(nextLocation)
                # nextLocation = [nextLocation[0], nextLocation[1]]
                if mapping.isInsideRink(nextLocation[0], nextLocation[1]):
                    moveAckerman(nextLocation)
                    break
                else:
                    print("need to turn")
            else:
                for t in range(1000, 2, -1):
                    degree = -math.pi/t 
                    print("turning ", degree)
                    nextLocation = ackermanService.turn(degree,ackerman, moveDistance)
                    drawPointAtLocal(nextLocation)
                    if ackerman.currentLocation[0] > 683 and ackerman.currentLocation[1] > 154 and nextLocation[0] < 685:
                        print("I'm there")
                    # nextLocation = [nextLocation[0], nextLocation[1]]
                    if mapping.isInsideRink(nextLocation[0], nextLocation[1]):
                        moveAckerman(nextLocation)
                        break
                    else:
                        print("need to turn more")



def resurface():
    enterRink()
    firstLap()


def main():
    pygame.init()

    resurface()

    # while True:
    #     screen.fill((0,0,0))
    #     rink_service.draw_dock(mapping,presets.dock[0],presets.dock[1])
    #     rink_service.drawRink(mapping)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             keepRunning = False
    #             break
    #     # ackermanService.move(ackerman, endLocal)
    #     ackermanService.draw(screen, ackerman)
    #     pygame.display.update()
    #     # checkArrived(ackerman, endLocal)
    #     # time.sleep(.05)
    # pygame.quit()

#Needed Global Variables
rink_service = RinkService()
importService = ImportService()
importService.setFile("config_assignment3.json")
presets = importService.getPresets()
startLocal = presets.startLocation
img = pygame.image.load('images/zoomboni.png')
img = pygame.transform.scale(img, (40, 20))
ackerman = Ackerman(currentLocation=startLocal, maxSteeringAngle=math.radians(presets.maxSteeringAngle), facingDirection=presets.facingDirection,velocity=5, length=.8, img=img)
ackermanService = AckermanService()
mapping = rink_service.determine_rink(presets.name)
screen = mapping.display


if __name__ == "__main__":
    main()
