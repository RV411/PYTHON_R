from cProfile import label
from re import X
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=np.linspace(0,10,20)
y=x*X
z=x+y

plt.plot(x,y,label='first example',color='b', lw=2, linestyle=':'#color='b g r'    linestyle=': - -. --'
                                ,marker='o',markersize=10, markerfacecolor='red',markeredgecolor='g',markeredgewidth=4)
plt.legend(loc=1)   #loc=1-10
plt.title('titulo')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#object oriented plots
fig=plt.figure()
x1=fig.add_axes([0.1,0.1,0.8,0.8])
x1.plot(x,y,y,x)

x1.set_xlabel('x-axis')
x1.set_ylabel('y-axis')
x1.set_title('title')

x1.set_xlim(0,10)
x1.set_ylim(0,60)

x2=fig.add_axes([0.4,0.4,0.3,0.3])
x2.plot(y,y)


fig,axes=plt.subplot(1,4,figsize=(10,3))
axes[0].plot(x,y)
axes[4].plot(x,y)
#plt.tight_layout()


#subplot        se enumenran del 1 al 6
plt.subplot(3,2,1)
plt.plot(x,x)   #linear
plt.subplot(3,2,2)
plt.hist(y,y)   #histograma
plt.subplot(3,2,3)
plt.bar(x,x)    #barras
plt.subplot(3,2,4)
plt.scatter(x,x)    #puntitos
plt.subplot(3,2,5)
plt.fill(x,x)       #lleno
plt.subplot(3,2,6)
plt.polar(x,y)


################################################################################
###########################    DOCUMENTATION  ##################################
################################################################################

#https://matplotlib.org/stable/tutorials/introductory/usage.html

