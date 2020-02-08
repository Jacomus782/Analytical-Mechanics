"""
===========================
The double pendulum problem
===========================

This animation illustrates the double pendulum problem.
"""

# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

import math

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np
import scipy.integrate as integrate
from matplotlib import patches
from numpy import sin, cos

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


# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.01
t = np.arange(0.0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 50
w1 = 0.0
th2 = 1.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1 * sin(y[:, 0])
y1 = -L1 * cos(y[:, 0])

x2 = L2 * sin(y[:, 2]) + x1
y2 = -L2 * cos(y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-Lmax, Lmax), ylim=(-Lmax, Lmax))
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

plumb_line_y = np.linspace(0, -Lmax, 100)
plumb_line_x = plumb_line_y * 0
plt.plot(plumb_line_x, plumb_line_y, 'k--', alpha=0.5)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i * dt))

    angle1 = math.degrees(np.arctan2(x1[i], y1[i]))
    if angle1 > 0:
        c1 = pat.Arc((0, 0), Lmax/2, Lmax/2, 90, 180, -angle1)
    else:
        c1 = pat.Arc((0, 0), Lmax / 2, Lmax / 2, 90, -angle1, 180)
    ax.add_patch(c1)
    return line, time_text, c1

#def angle_find(pos_x, pos_y):
#    angle = 90 + math.degrees(np.arctan2(pos_x, pos_y))
#    return angle


ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                              interval=25, blit=True, init_func=init)
# ani.save('double_pendulum.mp4', fps=15)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
