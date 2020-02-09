from Double_Pendulum import angle1_raw, time
import numpy as np
import matplotlib.pyplot as plt

angle1_raw = np.array(angle1_raw)
angle1_converted = []

for i in range(len(angle1_raw)):
    if angle1_raw[i] > 0:
        angle1_converted.append(180 - angle1_raw[i])
    else:
        angle1_converted.append(-(180 + angle1_raw[i]))
