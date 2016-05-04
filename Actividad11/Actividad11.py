
# coding: utf-8

# In[10]:

# zombie apocalypse modeling
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

P = 0           # birth rate
d = 0.0001  # natural death percent (per day)
B = 0.0095  # transmission percent  (per day)
G = 0.0001  # resurect percent (per day)
A = 0.0001  # destroy percent  (per day)
o = 0.0001
# solve the system dy/dt = f(y, t)
def f(y, t):
    Si = y[0]
    Zi = y[1]
    Ri = y[3]
    Ii = y[2]
    # the model equations (see Munz et al. 2009)
    f0 = P - B*Si*Zi - d*Si
    f1 = B*Si*Zi + G*Ri - A*Si*Zi
    f3 = B*Si*Zi-o-d*Ii
    f2 = d*Si+d*Ii+ A*Si*Zi - G*Ri
    
    return [f0, f1, f2,f3]

# initial conditions
S0 = 500.                   # initial population
Z0 = 0                      # initial zombie population
R0 = 0                      # initial death population
I0 = 0
y0 = [S0, Z0, R0,I0]   # initial condition vector
t  = np.linspace(0, 5., 1000)       # time grid

# solve the DEs
soln = odeint(f, y0, t)
S = soln[:, 0]
Z = soln[:, 1]
R = soln[:, 2]
I = soln[:, 3]
# plot results
plt.figure()
plt.plot(t, S, label='Living')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.title('Zombie Apocalypse - No Init. Dead Pop.; No New Births.')
plt.legend(loc=0)




# In[ ]:



