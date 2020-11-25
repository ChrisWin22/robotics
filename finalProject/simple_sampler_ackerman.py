import numpy as np
from matplotlib import pyplot as plt
import math

goal_state = [-10, -30, None]
vel = 5
del_t = 0.1
test = False
iter_limit = 150  # (15 second trajectory maximum)

def propogate(state, control):
    # State[0] = x, state[1] = y, state[2] = theta
    # control[0] = alpha
    next_state = [None, None, None]
    next_state[2] = state[2] + vel / 2.5 * math.tan(control[0]) * del_t  # Assume L=2.5
    next_state[0] = state[0] + math.sin(next_state[2])*vel*del_t
    next_state[1] = state[1] + math.cos(next_state[2])*vel*del_t

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


def distance(cur_state):
    return math.sqrt((goal_state[0] - cur_state[0])**2 + (goal_state[1] - cur_state[1])**2)


def go_to_goal():
    cur_state = [0, 0, math.pi/4]
    states_vec = []
    controls_vec = []
    states_vec.append(cur_state)
    control_samples = [-math.pi / 4, -math.pi / 8, 0, math.pi / 8, math.pi / 4]  # Set 5 samples between -45 to 45 degrees

    for i in range(iter_limit):
        if distance(cur_state) > 0.8:
            best_sample_dist = 1000000
            best_sample_state = [None, None, None]
            best_sample_control = [None]
            for u in control_samples:
                new_state_sampled = propogate(cur_state, [u])
                sampled_dist = distance(new_state_sampled)
                if sampled_dist < best_sample_dist:
                    best_sample_dist = sampled_dist
                    best_sample_state = new_state_sampled
                    best_sample_control = [u]
            cur_state = best_sample_state
            states_vec.append(cur_state)
            controls_vec.append(best_sample_control)
            if i == iter_limit-1:
                print('Goal not found after {} time steps, the iteration limit may need to be increased'.format(iter_limit))
                return states_vec, controls_vec
        else:
            print('Obtained goal location to within tolerance')
            return states_vec, controls_vec




if test:
    test_prop()
else:
    states_vector, controls_vector = go_to_goal()
    np_states = np.array(states_vector)
    plt.plot(np_states[:, 0], np_states[:, 1], 'b*')
    plt.show()
