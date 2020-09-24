import numpy as np

from matplotlib import pyplot as plt

import math

 

goal_state = [10, 20, None]

vel = 5

del_t = 0.1

test = True

L = 1

 

def propogate(state, control):

    # State[0] = x, state[1] = y, state[2] = theta

    # control[0] = alpha

    next_state = [None, None, None]

    theta = math.radians(state[2])

    xDot = math.sin(theta)*vel*del_t
    yDot = math.cos(theta)*vel*del_t
    thetaDot = vel / L * math.tan(control[0]) * del_t # Assume L=1

    next_state[0] = state[0] + xDot

    next_state[1] = state[1] + yDot

    next_state[2] = state[2] + thetaDot

    print("Locations: ", next_state)
 

    return next_state

 

def test_prop():

    cur_state = [0, 0, 45]

    states_vec = []

    states_vec.append(cur_state)

    for i in range(100):

        alpha = math.pi/4

        new_state = propogate(cur_state, [alpha])

        cur_state = new_state

        states_vec.append(cur_state)

 

    np_states = np.array(states_vec)

    plt.plot(np_states[:, 0], np_states[:, 1], 'b*')

    plt.show()

 

test_prop()