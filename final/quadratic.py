import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
from numpy.random import default_rng

rng = default_rng()

def draw_contours(fl,x,y,levels=[1]):
    X,Y = np.meshgrid(x,y)
    fig,axes = plt.subplots(1,len(fl))
    for ax,f in zip(axes,fl):
        ax.contour(X,Y,f(X,Y),levels)
    return fig


def Q1(x,y):
    return x**2 - y**2 


def Q2(x,y):
    return (1./4)*x**2 + (1./9)*y**2 


QL = [Q1,Q2]

af=draw_contours(QL, x=np.linspace(-5,5,25), y=np.linspace(-5,5,25))

af.savefig("quadratic.png")
