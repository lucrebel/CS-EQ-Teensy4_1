#Let's start building a digital hardware EQ, SSL Style! YILLEH

#Importing required library
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,5*np.pi,0.1)

#normal sine wave
y1 = np.sin(x)

#higher frequency sine wave
y2 = np.sin(4*x)

# Plotting Sine Graph
fig, (ax_sin,ax_sum) = plt.subplots(2,1)

ax_sin.plot(x, y1)
ax_sin.plot(x,y2)


#plotting sum of both
y_sum = y1 + y2
ax_sum.plot(x,y_sum)


plt.show()