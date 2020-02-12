from Data_Extraction import angle2_converted, angle1_converted
from Double_Pendulum import time, th1, th2, M1, M2, L1, L2
import matplotlib.pyplot as plt

plt.plot(angle1_converted, angle2_converted)
plt.xlabel('Angle 1 (°)')
plt.ylabel('Angle 2 (°)')
plt.title('A Graph Showing how Angle 1 Varies with Angle 2 Under the Initial Conditions:\n '
          'θ1 Initial = {}°, θ2 Initial = {}°, L1 = {} m, L2 = {} m, M1 = {} kg, M2 = {} kg'
          .format(th1, th2, L1, L2, M1, M2))


plt.show()