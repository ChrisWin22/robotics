import pygame
from movingDot import MovingDot
from movingDotService import MovingDotService
import time

pygame.init()

endLocal = [10, 10]

dot = MovingDot(currentLocation=[80,70])
dotService = MovingDotService()

objects = [dot]

keepRunning = True
screen = pygame.display.set_mode((100, 100))

while keepRunning:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False
            break
    for obj in objects:
        dotService.move(obj, endLocal)
        print(dot.currentLocation)
        dotService.draw(screen, obj)
    pygame.display.update()
    tempX = endLocal[0] - dot.currentLocation[0]
    tempY = endLocal[1] - dot.currentLocation[1]
    if (tempX < 1 and tempX > -1) and (tempY < 1 and tempY > -1):
        time.sleep(3)
        keepRunning = False
    time.sleep(.05)
pygame.quit()