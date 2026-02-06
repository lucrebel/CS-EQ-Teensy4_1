#Here we're going to use continuous transfer functions with scipy to create a low pass filter.
#Inspired by: https://www.youtube.com/watch?v=HJ-C4Incgpw

from scipy import signal
import numpy as np
pi = np.pi

#Continuous transfer function

w0 = 2*pi*5 #CUTOFF FREQUENCY (a.k.a. pole frequency)

num = w0

den = [1,w0]

lowpass = signal.TransferFunction(num,den) #TRANSFER FUNCTION

print(lowpass)


##LAST WEGNEHMEN VON TEENSY -Y wir stellen die funktion in diskreter form dar wegen der clock und loop frequency
dt = 1.0/1000.0 #Sampling frequency
discrete_lowpass = lowpass.to_discrete(dt,method='gbt',alpha = 0.5)
print(discrete_lowpass)

#Difference Equation? 
b = discrete_lowpass.num
a = -discrete_lowpass.den

print("Filter coeff. b_i: " + str(b))
print("Filter coeff. a_i: " + str(a[1:]))
