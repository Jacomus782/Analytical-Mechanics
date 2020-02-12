from Data_Extraction import angle2_converted, angle1_converted
from Double_Pendulum import time, th1, th2
import matplotlib.pyplot as plt

plt.plot(angle1_converted, angle2_converted)
plt.xlabel('Angle 1 (°)')
plt.ylabel('Angle 2 (°)')
plt.title('A graph showing how angle 1 varies with angle 2 under the initial conditions of angle 1 = {} and angle 2 = {}'.format(th1, th2))

plt.show()