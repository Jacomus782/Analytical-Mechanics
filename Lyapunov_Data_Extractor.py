from Double_Pendulum import dt, x1, y1
import math
import numpy as np

f = open("Data.txt", "a")

angle1_initial = math.degrees(np.arctan2(x1[0], y1[0]))
angle1_stepped = math.degrees(np.arctan2(x1[1], y1[1]))

f.write('{}, {}\n'.format(str(angle1_initial), dt*0))
f.write('{}, {}\n'.format(str(angle1_stepped), dt*1))
f.write('\n')



f.close()
