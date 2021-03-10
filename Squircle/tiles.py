import numpy as np
from numpy import pi, sqrt, cos, sin, sign
import matplotlib.patches as mpatches
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

def drawNestedShapes(axe,s, rSpan):
	t = np.linspace(0,2*pi,1000)
	for i in range(len(rSpan)):
		r = rSpan[i]
		[x,y] = FG_param1(r,s,t)
		axe.plot(x+2,y+2,'b')
		axe.plot(x+2,y-2,'b')
		axe.plot(x-2,y+2,'b')
		axe.plot(x-2,y-2,'b')

		return axe

xlim = [-3,3]
ylim = [-3,3]

r_min = 0.1
r_max = 4

nIters = 50
nPlots = 2
sSpan = np.linspace(0,1,nPlots)
rSpan = np.linspace(r_min,r_max,nIters)
fig, ax = plt.subplots(nPlots,2)
print(ax)
for i in range(nPlots):
	print(rSpan)
	test = drawNestedShapes(ax[i,0],sSpan[i], rSpan)
	plt.show()
	ax[i,0].plot(x+2,y+2,'b')
	ax[i,0].plot(x+2,y-2,'b')
	ax[i,0].plot(x-2,y+2,'b')
	ax[i,0].plot(x-2,y-2,'b')
	ax[i,0].set_xlim(-5,5)
	ax[i,0].set_ylim(-5,5)

	ax[i,1] = ax[i,1]
	ax[i,1].set_xlim(-1,1)
	ax[i,1].set_ylim(-1,1)

plt.grid(False)
plt.axis('Off')
ax = plt.gca()
ax.set_aspect('equal')
plt.show()


'''

for i in range(nIters):
	r = rSpan[i]
	[x,y] = FG_param1(r,s,t)
	ax.plot(x+2,y+2,'b')
	ax.plot(x+2,y-2,'b')
	ax.plot(x-2,y+2,'b')
	ax.plot(x-2,y-2,'b')
	return ax 
	
plt.grid(False)
plt.axis('Off')
ax = plt.gca()
ax.set_aspect('equal')
plt.xlim(xlim)
plt.ylim(ylim)
plt.show()

'''
'''
plt.grid(False)
plt.axis('off')
plt.savefig('%dsines.svg' % M)
plt.savefig('%dsines.png' % M)
plt.show()
'''

