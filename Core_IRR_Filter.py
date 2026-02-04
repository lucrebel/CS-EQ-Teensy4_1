#In this document we'll be learning the basics on filtering using the scipy library.

import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

#First we'll generate to input signals and their superposition
#(first index, end, step size)
x = np.arange(0,5*pi,0.1) #For x-Axis on plot

y1 = np.sin(x)
y2 = np.sin(20*x)

#Superposition
y_res = y1+y2


##SIMPLE FILTER

#Create empty array of same lenths y1 = y2 = y_res
y_out = np.zeros(len(y_res))

#Scaling factor for filter -> big value a ->Fast changes get through, Highpass filter ! 
a = 0.1

#Iterate through each element in y_res 
for i in range(len(y_res)):

    y_out[i] = a * y_res[i] + (1-a) * y_out[i-1]



# Plotting Sine Graph
fig, (ax_sin,ax_out) = plt.subplots(2,1)

ax_sin.plot(x, y_res)

ax_out.plot(x,y_out)



#Plot output
plt.show()