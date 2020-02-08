#Taken from http://systems-sciences.uni-graz.at/etextbook/sw2/lyapunov.html
from typing import Any, Union

import numpy as np
import matplotlib.pyplot as plt
import math
from decimal import Decimal
# show plots in notebook
#% matplotlib inline

result = []
lambdas = []
maps = []

# define range of r
rvalues = np.arange(0, 2, 0.01)

# loop through r
for r in rvalues:
    x = 0.1
    result = []
    # iterate system 100 times
    for t in range(100):
        x = x + r - x ** 2
        # calculate log of the absolute of the derivative
        if 1-2*x != 0:
            result.append(math.log(abs(1 - 2 * x)))
        else:
            pass
    # take average
    lambdas.append(np.mean(result))
    # for the map ignore first 100 iterations as transient time and iterate anew
    for t in range(20):
        x = x + r - x ** 2
        maps.append(x)

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(1, 1, 1)

xticks = np.linspace(0, 2, 4000)
# zero line
zero = [0] * 4000
ax1.plot(xticks, zero, 'g-')
# plot map
ax1.plot(xticks, maps, 'r.', alpha=0.3, label='Map')
ax1.set_xlabel('r')
# plot lyapunov
ax1.plot(rvalues, lambdas, 'b-', linewidth=3, label='Lyapunov exponent')
ax1.grid('on')
ax1.set(ylim=(-4, 4))
ax1.set_xlabel('r')
ax1.legend(loc='best')
ax1.set_title('Map of x(t+1) = x(t) + r - x(t)^2 versus Lyapunov exponent')
plt.show(fig)