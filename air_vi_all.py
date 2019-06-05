import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

'''
F = g - Ar
Ar = aV

F = g - aV

v' = (g - av)/m


'''

def solver(g, a, m, dt, T, vi):
    dt = float(dt)
    Nt = round(int(T/dt))
    u = np.zeros(Nt+1)
    t = np.linspace(0, Nt*dt, Nt + 1)

    u[0] = vi

    for n in range(0, Nt ):
        u[n + 1] = (((g*dt)) + (u[n])*(1 - (a*dt)/(2*m)))/(1 + (a*dt)/(2*m))

    return u, t


def creategraph(vi):
    g = 9.8
    a = 2
    T = 500
    dt = 0.01

    m = 1      
    u, t = solver(g, a, m, dt, T, vi)
    plt.plot(t, u, 'C0-')

    m = 5      
    u, t = solver(g, a, m, dt, T, vi)
    plt.plot(t, u, 'C1-')

    m = 20      
    u, t = solver(g, a, m, dt, T, vi)
    plt.plot(t, u, 'C2-')

    m = 50      
    u, t = solver(g, a, m, dt, T, vi)
    plt.plot(t, u, 'C3-')

    m = 100      
    u, t = solver(g, a, m, dt, T, vi)
    plt.plot(t, u, 'C4-')

    umin = 0; umax = 1.2*u.max()
    plt.title('Velocity in free fall with air resistance\na=%g, vi=all' % (a) )
    plt.legend(['m=1', 'm=5', 'm=20', 'm=50', 'm=100'], loc='upper right')
    plt.xlabel('t')
    plt.ylabel('v')
    plt.axis([t[0], t[-1], umin, umax])
    plt.savefig('f1_viall.png')

for x in [0, 10, 50]:
    creategraph(x)
for x in range(1, 11):
    creategraph(100*x)