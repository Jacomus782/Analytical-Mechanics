from Double_Pendulum import angle1_raw, angle2_raw
import numpy as np

angle1_raw = np.array(angle1_raw)
angle1_converted = []

for i in range(len(angle1_raw)):
    if angle1_raw[i] > 0:
        angle1_converted.append(180 - angle1_raw[i])
    else:
        angle1_converted.append(-(180 + angle1_raw[i]))

angle2_converted = []
# Function needs verifying
for i in range(len(angle2_raw)):
    if angle2_raw[i] > 0:
        angle2_converted.append(180 - angle2_raw[i])
    else:
        angle2_converted.append(-(180 + angle2_raw[i]))
