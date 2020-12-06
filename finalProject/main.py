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
    distance = math.sqrt(tempX ** 2 + tempY ** 2)
    if distance < 5:
        return True
    return False
    # if (tempX < 1 and tempX > -1) and (tempY < 1 and tempY > -1):
    #     return True
    # return False

def drawHistory():
    for location in ackerman.visited:
        pygame.draw.circle(screen, ackerman.pathColor, [location[0], location[1]], 10, 0)

    ackerman.pathIncrement = ackerman.pathIncrement + 1
    if ackerman.pathIncrement == 50:
        ackerman.visited.append(ackerman.currentLocation)
        ackerman.pathIncrement = 0

def moveAckerman(moveTo):
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        rink_service.draw_dock(mapping,presets.dock[0],presets.dock[1])
        rink_service.drawRink(mapping)

        drawHistory()

        ackermanService.move(ackerman, moveTo)
        ackermanService.draw(screen, ackerman)
        pygame.display.update()
        if checkArrived(ackerman, moveTo):
            return

def getTopRightOfRink(offset):
    r = mapping.radius * mapping.SCALAR + 15 + offset
    tempX = r*math.cos(45)
    tempY = r*math.sin(45)
    xDot = r - tempX
    yDot = r - tempY
    x = mapping.left + xDot
    y = mapping.top + yDot
    drawPointAtLocal([x,y])
    return [x,y]

def enterRink(offset):
    entranceLocal = presets.dock[0], presets.dock[1]
    moveAckerman(entranceLocal)
    rinkOpening = presets.dock[0] + (4.7*mapping.SCALAR), presets.dock[1] + (2.3*mapping.SCALAR)/2
    # moveAckerman(rinkOpening)
    
    #Move to top left of rink
    moveAckerman(getTopRightOfRink(offset))

    # moveAckerman(mapping.rink.center)

def drawPointAtLocal(local):
    pygame.draw.circle(screen, [0,255,0], [local[0],local[1]], 5, 0)
    pygame.display.update()

def finishedLap(nextLocation, offset):
    global timer
    distance = nextLocation[0] - (mapping.left + offset)
    if distance < 15 and timer > 5:
        finished = ackermanService.hasVisited(ackerman, nextLocation[0], nextLocation[1])
        if finished == True:
            timer = 0
        return finished
    # if ackerman.currentLocation[1] < presets.dock[1] or ackerman.currentLocation[1] > presets.dock[1] + (2.3*mapping.SCALAR):
    #     return False
    # if math.sqrt(ackerman.currentLocation[0] ** 2 + (mapping.left + offset) ** 2) > 10:
    #     return False
    # return True


def lap(offset=0):
    global timer
    # endLocal = getTopRightOfRink(offset)
    turningOptions = [0, 1]
    moveDistance = 3
    while True:
        for o in turningOptions:
            if o == 0:
                nextLocation = ackermanService.turn(o,ackerman, moveDistance)
                drawPointAtLocal(nextLocation)
                if finishedLap(nextLocation, offset):
                    return
                # nextLocation = [nextLocation[0], nextLocation[1]]
                if mapping.isInsideRink(nextLocation[0], nextLocation[1], offset):
                    timer += 1
                    moveAckerman(nextLocation)
                    print("=" * 25)
                    print("Moved to: ", ackerman.currentLocation)
                    break
            else:
                for t in range(1000, 2, -1):
                    degree = -math.pi/t 
                    nextLocation = ackermanService.turn(degree,ackerman, moveDistance)
                    drawPointAtLocal(nextLocation)
                    if finishedLap(nextLocation, offset):
                        return
                    # nextLocation = [nextLocation[0], nextLocation[1]]
                    if mapping.isInsideRink(nextLocation[0], nextLocation[1], offset):
                        timer += 1
                        moveAckerman(nextLocation)
                        print("=" * 25)
                        print("Moved to: ", ackerman.currentLocation)
                        break
        
def moveToStartingPlace(offset):
    moveAckerman(getTopRightOfRink(offset + 40))



def resurface():
    deltaOffset = 15
    startingOffset = 10
    currentOffset = startingOffset
    enterRink(currentOffset)


    while True:
        # enterRink(currentOffset)
        lap(currentOffset)
        print("End of lap ", currentOffset/10)
        currentOffset += deltaOffset
        # moveToStartingPlace(currentOffset)
        nextLocal = ackermanService.turn(-math.pi/6, ackerman, 6)
        moveAckerman(nextLocal)




def main():
    pygame.init()
    # ackerman.currentLocation = [127.71682584204702, 316.671844709084, -1.9792726740856632]
    # ackerman.facingDirection = -1.9792726740856632
    rink_service.draw_dock(mapping,presets.dock[0],presets.dock[1])
    rink_service.drawRink(mapping)
    ackermanService.draw(screen, ackerman)


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
global timer
timer = 0
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
