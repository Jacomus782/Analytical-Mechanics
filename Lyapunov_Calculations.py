import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from numpy import sin, cos
from statistics import mean

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg
Lmax = L1 + L2

def derivs(state, t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (M1 + M2) * L1 - M2 * L1 * cos(del_) * cos(del_)
    dydx[1] = (M2 * L1 * state[1] * state[1] * sin(del_) * cos(del_) +
               M2 * G * sin(state[2]) * cos(del_) +
               M2 * L2 * state[3] * state[3] * sin(del_) -
               (M1 + M2) * G * sin(state[0])) / den1

    dydx[2] = state[3]

    den2 = (L2 / L1) * den1
    dydx[3] = (-M2 * L2 * state[3] * state[3] * sin(del_) * cos(del_) +
               (M1 + M2) * G * sin(state[0]) * cos(del_) -
               (M1 + M2) * L1 * state[1] * state[1] * sin(del_) -
               (M1 + M2) * G * sin(state[2])) / den2
    return dydx

def factor_calc(diverg, initial):
    factor = (1/dt)*np.log(abs(diverg)/abs(initial))
    return factor

def vector_mag(x, y):
    length = math.sqrt(x ** 2 +y ** 2)
    return length

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.01
t = np.arange(0.0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 40
w1 = 0
th2 = 0
w2 = 0
dth1 = 0.01
dth2 = 0.01
dw1 = 0
dw2 = 0


angle1_array = []
angle2_array = []
momentum1_array = []
momentum2_array = []
factor_array = []



vector_array = []

for i in range(5):
    state = np.radians([th1 - dth1*i, w1 - dw1*i , th2 - dth2*i, w2 - dw2*i])

    y = integrate.odeint(derivs, state, t)

    x1 = L1 * sin(y[:, 0])
    y1 = -L1 * cos(y[:, 0])

    x2 = L2 * sin(y[:, 2]) + x1
    y2 = -L2 * cos(y[:, 2]) + y1

    initial_angle1 = math.degrees(np.arctan2(x1[0], y1[0]))
    initial_angle2 = math.degrees(np.arctan2(x2[0], y2[0]))

    angle1 = math.degrees(np.arctan2(x1[1], y1[1]))
    angle1_array.append(angle1)

    angle2 = math.degrees(np.arctan2(x2[1], y2[1]))
    angle2_array.append(angle2)
    if i == 0:
        vector_0 = vector_mag(angle1_array[0] - initial_angle1, angle2_array[0] - initial_angle2)
    else:
        vector_array.append(vector_mag(angle1_array[0] - initial_angle1, angle2_array[0] - initial_angle2))
    # momentum1 = y[0, 0]
    # momentum1_array.append(momentum1)

    # momentum2 = y[0, 2]
    # momentum2_array.append(momentum2)

    #factor_array.append(factor_calc(angle1_array[i], initial_angle1))
vector_average = mean(vector_array)

lyapunov_exponent = factor_calc(vector_average, vector_0)

angles = []
exponents = []

angles.append(th1)
exponents.append(lyapunov_exponent)

plt.plot(x, y)

print(lyapunov_exponent)

