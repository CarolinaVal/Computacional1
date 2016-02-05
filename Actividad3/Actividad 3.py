
# coding: utf-8

# In[2]:

import numpy as perrito
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

x00 = perrito.random.random(10)
x0=3*x00

y0 = perrito.sin(2*x0)

plt.plot(x0, y0, 'o', label='Data')

x=perrito.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)
    plt.plot(x, f(x), label=o)

plt.legend()
plt.show()


# In[1]:

import numpy as perrito
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

x00 = perrito.random.random(20)
x0=20*x00-10
y0 = perrito.sin(x0)/x0

plt.plot(x0, y0, 'o', label='Data')

x=perrito.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)
    plt.plot(x, f(x), label=o)
plt.legend()
plt.show()


# In[2]:

import numpy as perrito
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

x00 = perrito.random.random(16)
x0=6*x00-3
y0 = x0**2*perrito.sin(2*x0)

plt.plot(x0, y0, 'o', label='Data')



x=perrito.linspace(min(x0), max(x0), 101)
options = ('linear', 'quadratic', 'cubic')

for o in options: 
    f = interp1d(x0, y0, kind=o)
    plt.plot(x, f(x), label=o)
    
plt.legend()
plt.show()


# In[3]:

import numpy as perrito
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

x00 = perrito.random.random(12)
x0=4*x00-2
y0 = x0**3*perrito.sin(3*x0)

plt.plot(x0, y0, 'o', label='Data')

x =perrito.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)
    plt.plot(x, f(x), label=o)

plt.legend()
plt.show()


# In[3]:




# In[ ]:



