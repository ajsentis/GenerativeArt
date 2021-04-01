import numpy as np
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt

t = np.linspace(-5*np.pi,0*np.pi,1000)

M =10
for iPlot in range(1,M+1):
  for i in range(iPlot):
    print(iPlot,i)
    y = np.cos(t*1/(1-0.07*i)+0*i*2*np.pi/iPlot)
    plt.plot(t,y+(3*(iPlot-1)-M),color='k',linewidth=0.9)


plt.grid(False)
plt.axis('off')
plt.savefig('%dsines.svg' % M)
plt.savefig('%dsines.png' % M)
plt.show()


