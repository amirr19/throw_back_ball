#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
v_zero = 30
start_time = 0
end_time = (2*v_zero*math.sin(0.96))/(9.8)


# In[2]:


class Passway:
    def __init__ (self, teta):
        x_arr = []
        y_arr = []
        t_arr = []
        for t in np.arange (start_time,end_time,0.1):
            t = round(t , 1)
            x = (-3.45)*(t**2)+(v_zero *math.cos(teta) * t)
            x_arr.append(x)
            y = (-4.9)*(t**2)+(v_zero *math.sin(teta) * t)
            y_arr.append(y)
            t_arr.append(t)
        self.teta = teta
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.t_arr = t_arr
        


# In[8]:


p1 = Passway(0.96)
p2 = Passway(0.5)
p3 = Passway(1.5)


# In[9]:


Pass = [p1,p2,p3]
for p in Pass:
    figure(num=None, figsize=(1,1), dpi=100, facecolor='w', edgecolor='k')
    fig, (ax1,ax2,ax3) = plt.subplots(1,3)
    
    fig.suptitle('teta = '+ str(p.teta)+'Rad')
    
    
    ax1.plot(p.x_arr,p.t_arr)
    ax1.set(xlabel='x', ylabel='t')
    ax1.set_title('X')
    
    ax2.plot(p.t_arr,p.y_arr)
    ax2.set(xlabel='t', ylabel='y')
    ax2.set_title('Y')

    ax3.plot(p.x_arr,p.y_arr)
    ax3.set(xlabel='x', ylabel='t')
    ax3.set_title('x,y')


# In[ ]:





# In[ ]:




