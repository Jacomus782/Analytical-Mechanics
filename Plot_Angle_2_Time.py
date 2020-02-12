from Data_Extraction import angle2_converted, angle1_converted
from Double_Pendulum import time, th1, th2, M1, M2, L1, L2
import matplotlib.pyplot as plt

plt.plot(time, angle2_converted)
plt.xlabel('Time (s)')
plt.ylabel('Angle (°)')
plt.title('A Graph Showing how Angle 2 Varies with Time Under the Initial Conditions:\n '
          'θ1 Initial = {}°, θ2 Initial = {}°, L1 = {} m, L2 = {} m, M1 = {} kg, M2 = {} kg'
          .format(th1, th2, L1, L2, M1, M2))


plt.show()