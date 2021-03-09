import numpy as np
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt

t = np.linspace(0,10*np.pi,1000)

M =10
for iPlot in range(1,M+1):
  for i in range(iPlot):
    print(iPlot,i)
    y = np.sin(t+i*2*np.pi/iPlot)
    plt.plot(t,y+(3*(iPlot-1)-M),color='blue',linewidth=0.5)


plt.grid(False)
plt.axis('off')
plt.savefig('%dsines.svg' % M)
plt.savefig('%dsines.png' % M)
plt.show()

'''
plt.plot(t,-3+np.sin(t))
plt.plot(t,np.sin(t))
plt.plot(t,np.sin(t+np.pi))
plt.plot(t,3+np.sin(t))
plt.plot(t,3+np.sin(t+np.pi/3))
plt.plot(t,3+np.sin(t+2*np.pi/3))
'''
#plt.axis('equal')

