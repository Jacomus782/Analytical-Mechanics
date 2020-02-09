from Data_Extraction import angle2_converted
from Double_Pendulum import time, th1, th2
import matplotlib.pyplot as plt

plt.plot(time, angle2_converted)
plt.xlabel('Time (s)')
plt.ylabel('Angle (°)')
plt.title('A graph showing how angle 2 varies with time under the initial conditions of angle 1 = {} and angle 2 = {}'.format(th1, th2))

plt.show()