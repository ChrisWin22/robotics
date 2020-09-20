import matplotlib.pyplot as plt
from matplotlib import animation
import json
import numpy as np
import os
import keyboard     
import math    

config = json.load(open('firstSimulation/config_assignment2.json'))
start = config['start']
goal = config['goal']
maxVelocity = config['maxVelocity']
minVelocity = 0


target_angle = math.atan((goal[1] - start[1])/(goal[0] - start[0]))
# if((goal[1] - start[1]) < 0 or (goal[0] - start[0]) < 0):
#     target_angle = target_angle
target_pos = [goal[0], goal[1]]
startingLocation = [start[0],start[1]]
currentLocation = startingLocation
velocity = 1
print(goal)

def canMove(currentLocation, i):
    dist1 = [goal[0] - currentLocation[0], goal[1] - currentLocation[1]]
    dist2 = np.sqrt(dist1[0] ** 2 + dist1[1] ** 2)
    if (i/10 * velocity) <= dist2:
        return True
    return False

def updateVelocity():
    global velocity
    if keyboard.is_pressed('w') and velocity != maxVelocity:
        print("increase speed")
        velocity += 1
    if keyboard.is_pressed('r') and velocity != minVelocity:
        print("decrease speed")
        velocity -= 1

def animate(i):
    global currentLocation
    updateVelocity()
    if canMove(currentLocation, i):
        if(currentLocation[0] < goal[0]):
            currentLocation[0] += ((i/10 * velocity) * math.cos(target_angle))
        else:
            currentLocation[0] -= ((i/10 * velocity) * math.cos(target_angle))
        if(currentLocation[1] < goal[1]):
            currentLocation[1] += ((i/10 * velocity) * math.sin(target_angle))
        else:
            currentLocation[1] -= ((i/10 * velocity) * math.sin(target_angle))
        d.set_data(currentLocation[0], currentLocation[1])
        return d,

fig = plt.figure()
ax = plt.axes(xlim=(0,100), ylim=(0,100))
d, = ax.plot(currentLocation[0], currentLocation[1], 'bo')
anim = animation.FuncAnimation(fig, animate, frames=200, interval=200)
plt.show()