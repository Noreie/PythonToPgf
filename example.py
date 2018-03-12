import pytopgf as p2p
import numpy as np
import math

def ema(y, a):
    s = []
    s.append(y[0])
    for t in range(1, len(y)):
        s.append(a * y[t] + (1-a) * s[t-1])
    return np.array(s)

p2p.sexyplot() #Kan slås av
fig, ax  = p2p.newfig(345,ratio=1.5)



y = [0]*200
y.extend([20]*(1000-len(y)))
s = ema(y, 0.01)



ax.plot(s)
ax.set_xlabel('X Label')
ax.set_ylabel('EMA')
fig.show()
p2p.savefig("hallo")
