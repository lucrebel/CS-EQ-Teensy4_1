#In this document we'll be learning the basics on filtering using the scipy library.

import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

#First we'll generate to input signals and their superposition
#(first index, end, step size)
x = np.arange(0,5*pi,0.1) #For x-Axis on plot

y1 = np.sin(x)
y2 = np.sin(30*x)
y3 = np.sin(100*x)

#Superposition
y_res = y1+y2+y3


##SIMPLE FILTER

#Create empty array of same lenths y1 = y2 = y_res
y_lp = np.zeros(len(y_res))

#Scaling factor for filter -> big value a ->Fast changes get through, Highpass filter ! 
a_lp = 0.5

#Iterate through each element in y_res 
for i in range(len(y_res)):

    y_lp[i] = a * y_res[i] + (1-a) * y_lp[i-1]

#Now we have y_out that is a low pass filtered signal,
#if we subtract out y_out from y_res whe take out the low frequencies and have a highpass filter!
y_highpass = y_res - y_lp

#BANDPASS
y_bandpass = y_res - (y_out + y_highpass)




# Plotting Sine Graph
fig, (ax_sin,ax_out,ax_highpass,ax_bandpass) = plt.subplots(4,1)

ax_sin.plot(x, y_res)

ax_out.plot(x,y_out)

ax_highpass.plot(x,y_highpass)

ax_bandpass.plot(x,y_bandpass)



#Plot output
plt.show()