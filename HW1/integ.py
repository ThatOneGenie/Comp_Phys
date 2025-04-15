# -*- coding: utf-8 -*-
""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation
    
    Original code: TrapMethods.py
    
    2019: Extended by Lev Kaplan to include Simpson integration and loop over number of points"""

# integ.py: trapezoid and Simpson integration, a<x<b, N pts, N-1 intervals 

import matplotlib.pyplot as plt 
import numpy as np
import scipy.optimize as opt

def func(x):          # function to be integrated
    #return np.exp(-x)
    return np.sin(np.exp(5.0)*x+7.0)

def trapezoid(A,B,N):   #integrate from A to B using N points
    h = (B - A)/(N - 1)                     # step size 
    sum = (func(A)+func(B))/2               # (1st + last)/2
    for i in range(1, N-1):        # i goes from 1 to (N-1)-1
       sum += func(A+i*h)
#       sum=np.float32(sum)            # to simulate single-precision (32 bit) calculation
    return h*sum  

def simpson(A,B,N):
    if ((N-1)%2==1):     #  if number of intervals odd
        print("Simpson's rule requires even number of intervals")
        return 0
    h = (B - A)/(N - 1)                     # step size 
    sum = (func(A)+func(B))/3               # (1st + last)/3
    for i in range(1, N-1,2):        # i loops over odd integers  from 1 to (N-1)-1
       sum += 4/3*func(A+i*h)
 #      sum=np.float32(sum)
    for i in range(2, N-1,2):        # i loops over even integers starting with 2
       sum += 2/3*func(A+i*h)
#       sum=np.float32(sum)
    return h*sum  
def romberg(A,B,N):
    return (((16.0 *simpson(A, B, 2*N-1))-simpson(A, B, N))/15.0) 

A = 0.0
B = 1.0


maxpoints = 10**7
#%%
Nvalues = []    #empty lists
traperror = []
simperr = []
romberr = []
#%%
#exact = 1-np.exp(-1)  # Exact for exp(-x)
exact = (np.cos(7.0)-np.cos(7.0+np.exp(5.0)))/np.exp(5.0)  # Exact for sin(exp(5.0)*x+7.0)

N=3
while N<maxpoints:    # loop over number of points
    print(N)    #just so you can see while code is running
    Nvalues.append(N)
    traperror.append(abs(trapezoid(A,B,N)-exact)/exact) # Error in trapezoid method
    simperr.append(abs(simpson(A,B,N)-exact)/exact) # Error in Simpson method
    romberr.append(abs(romberg(A, B, N)-exact)/exact) # Error in Romberg method
    N=int(N*1.1)+1    # N grows roughly by 1.1 factor each time
    if N%2 == 0:
        N=N+1    # make sure N is odd
# %%
# Approximate the rounding error by curve fitting
def fit(x,s):
    return s*x
trapfit_data = traperror[60:76]
simpfit_data = simperr[60:76]
rombfit_data = romberr[0:16]
trapfit, trapcovar=opt.curve_fit(fit, Nvalues, traperror)
simpfit, simpcovar=opt.curve_fit(fit, Nvalues, simperr)
rombfit, rombcovar =opt.curve_fit(fit, Nvalues, romberr)
Narray = np.array(Nvalues)
print(traperror,simperr)
print(trapfit,simpfit,rombfit)




#%%
plt.loglog(Nvalues,traperror,label="Trapezoid Error", linewidth=2.5)   # log log plot of error in trapezoid method
plt.loglog(Nvalues, simperr, label="Simpson Error", linewidth=2.5) 
#plt.loglog(Nvalues,romberr, label="Romberg Error", linewidth=2.5, linestyle="solid")
plt.loglog(Nvalues, 0.1/(Narray**2), label=r"$\frac{0.1}{N^{2}}$", linestyle = "dashed", linewidth=1.5)
plt.loglog(Nvalues, 0.01/(Narray**4), label=r"$\frac{0.01}{N^{4}}$", linestyle = "dashed", linewidth=1.5)
#plt.loglog(Nvalues, 0.0001/(Narray**6), label=r"$\frac{0.0001}{N^{6}}$", linestyle = "dashed", linewidth=1.5)
plt.loglog(Nvalues, 10e-17*(Narray**0.5), label=r"$10^{-17}N^{\frac{1}{2}}$", linestyle="dashed", linewidth=1.5)
plt.ylim([1e-17,1e2])   # set range of y values
legend = plt.legend(loc="upper right", fontsize = 8)
plt.title(r"Integration on $f(x)=e^{-x}$", fontsize = 18)
plt.xlabel("Number of Points (N)", fontsize = 14)
plt.ylabel("Error", fontsize = 14)
plt.show()    #show the graph
# %%