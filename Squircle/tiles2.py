import numpy as np
from numpy import pi, sqrt, cos, sin, sign
import matplotlib
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt

def FG_param1(r, s, t):
    if s == 0:
        return r*cos(t), r*sin(t)
    sin_t = sin(t)
    cos_t = cos(t)
    radical = sqrt(1 - sqrt(1 - s**2 * sin(2*t)**2))
    x_denom = np.where(np.isclose(sin_t, 0.0), 1.0, s*sqrt(2)*np.abs(sin_t))
    x = r * sign(cos_t) * np.where(np.isclose(sin_t, 0.0, 1e-12), 1.0, radical / x_denom)
    y_denom = np.where(np.isclose(cos_t, 0.0), 1.0, s*sqrt(2)*np.abs(cos_t))
    y = r * sign(sin_t) * np.where(np.isclose(cos_t, 0.0, 1e-12), 1.0, radical / y_denom)
    return x, y

def plotTiles(nPlots, nIters,rMin, rMax):
	t = np.linspace(0,2*pi,1000)
	sSpan = np.linspace(0,1,nPlots)
	rSpan = np.linspace(rMin,rMax,nIters)
	fig = plt.figure()
	gs = fig.add_gridspec(nPlots,2, hspace=0.1, wspace = 0.1)
	ax = gs.subplots()
	for plot in range(nPlots):
		for r in rSpan:
			x,y = FG_param1(r, np.sqrt(sSpan[plot]), t)
			ax[plot,0].plot(x,y,'b',linewidth=0.5)
			ax[plot,1].plot(x,y,'b',linewidth=0.5)
		ax[plot,0].set_xlim(-rMax-0.5,rMax+0.5)
		ax[plot,0].set_ylim(-rMax-0.5,rMax+0.5)
		ax[plot,0].axis('Off')
		ax[plot,0].set_aspect('equal', 'box')

		ax[plot,1].set_xlim(-rMin-0.1,rMin+0.1)
		ax[plot,1].set_ylim(-rMin-0.1,rMin+0.1)
		ax[plot,1].set_aspect('equal', 'box')
		ax[plot,1].axis('Off')
	figure = ax
	return figure
r_min = 0.1
r_max = 4

nIters = 20
nPlots = 5
print()
tile = plotTiles(nPlots, nIters,r_min, r_max)

plt.grid(False)



plt.show()
