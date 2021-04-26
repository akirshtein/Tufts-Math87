import numpy as np
import numpy.linalg as la
from numpy.random import default_rng

rng = default_rng()


p10 = np.array([412,220,187,48])
p20 = np.array([378,352,221,96])
p30 = np.array([450,317,237,52])

f1 = np.array([.4,1.5,.65,.5])
s1 = np.array([.5,.5,.35])

f2 = np.array([.20,1,.65,.5])
s2 = np.array([.48,.5,.35])

f3 = np.array([.4,1.5,.55,.5])
s3 = np.array([.5,.5,.35])


def sbv(index,size):
    return np.array([1.0 if i == index else 0.0 for i in range(size)])

def M(f,s):
    return np.array([f] + [s[i]*sbv(i,4) for i in range(3)])


def noise(i):
    if i==0:
        return np.zeros(4)
    else:
        return -15*np.ones(4) + 30*rng.random(4)

def evolve(M,p):
    return np.array([noise(i) + la.matrix_power(M,i) @ p for i in range(6)]).T 

B1=evolve(M(f1,s1),p10)
B2=evolve(M(f2,s2),p20)
B3=evolve(M(f3,s3),p30)
