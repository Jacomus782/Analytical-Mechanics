from Double_Pendulum import x1, y1, angle1_raw
import numpy as np

angle1_raw = np.array(angle1_raw)
angle1_converted = []

for i in range(len(angle1_raw)):
    if angle1_raw[i] > 0:
        angle1_converted.append(180 - angle1_raw[i])
    else:
        angle1_converted.append(-(180 + angle1_raw[i]))

print(angle1_converted)
