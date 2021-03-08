import numpy as np
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt



x_bounds = [-10,10]
y_bounds = [-10,10]

numTries = 5
r_min = 0.1
r_max = 2
circles = []

'''
Draw circles:
1) Pick random point in the space
2) Check to make sure it is at least positive r_min from the nearest circle, if its not go back to (1)
3) Draw the circle as big as possible up to r_max
4) Save circle[i] as [x,y,r]
5) Repeat for numTries
'''

for i in range(numTries):
  cx, cy = np.random.uniform(*x_bounds),np.random.uniform(*y_bounds)
  c = np.array([cx,cy])
  r = max
  print(c)
