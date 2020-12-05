import time
import math
import matplotlib.pyplot as plt

def distance(cur_state, expected):
    return math.sqrt((expected[0] - cur_state[0])**2 + (expected[1] - cur_state[1])**2)


deltaTs = [1,.1,.01, .000000001]
endLocals = [None, None, None, None]
errors = [None, None, None]
errorCount = 0

for deltaT in deltaTs:
    curLocal = [0,0,math.pi/2]
    startTime = time.time()
    while (time.time() - startTime) < 10:
        curLocal[0] += math.sin(curLocal[2]) * 20 * deltaT
        curLocal[1] += math.cos(curLocal[2]) * 20 * deltaT
        curLocal[2] += 5 * math.tan(math.pi/6) * deltaT
    endLocals[errorCount] = curLocal
    errorCount += 1

for i in range(0,3):
    errors[i] = distance(endLocals[i], endLocals[3])

xValues = [1,.1,.01]
x_pos = [i for i, _ in enumerate(xValues)]
print(errors)
plt.bar(x_pos, errors)
plt.xticks(x_pos, xValues)
plt.show()