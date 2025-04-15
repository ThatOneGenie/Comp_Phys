""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation
    
    Adapted by Lev Kaplan 2019"""

# Lagrange.py: Langrange interpolation tabulated data
import matplotlib.pyplot as plt
import numpy as np

def legendrepol (x,beg,finish):          # poly interpolation at x 
    y = 0.                               # using input points from beg to finish
    for  i in range(beg,finish+1): 
       lambd = 1.0;
       for j in range(beg,finish+1):
           if i != j:                       #Lagrange polynom formed here
              lambd = lambd * ((x - xin[j])/(xin[i] - xin[j]))
       y += yin[i] * lambd
    return y

NMAX = 100  # max number of input points

xin = np.zeros(NMAX)  # each is array of length NMAX, all elements set to zero
yin = np.zeros(NMAX)

inputfile = open("lagrange.dat","r")  # read in the input x,y values
r = inputfile.readlines()  # read the whole file into list (one item per line)
inputfile.close()
        # input has the form: x0 y0
        #                    x1 y1
         #                   ...
m = 0
for i in np.linspace(-1,1, num=21):
    xin[m] = i
    yin[m] = 1.0/(1.0 + (25*i**2))
    print(xin[m],yin[m])
    m += 1

    

# m = 0
# for line in r:
#     #print(line)
#     s = line.split() # split line and split into list of items(assume items separated by spaces)
#     xin[m] = s[0] # first number in each line is the x value
#     yin[m] = s[1]
#     print(xin[m],yin[m])
#     m+=1         # m is total number of input data points
#                  # will be stored in xin[0]..xin[m-1],yin[0].yin[m-1]

xvalues=np.linspace(-1,1,201)  # At least 200 Steps needed to fully interpolate using our function. More will add fidelity
yval_glo = []
yval_lin = []
yval_cub = []

for x in xvalues:
    for i in range(0, m-1):
        if xin[i] <= x and x <= xin[i+1]:
            firstpoint = i
    # firstpoint = int(x/25)
    cubepoint = firstpoint
    if cubepoint > m-4:
         cubepoint = m-4        #Need highest cubpoint to be cubepoint+3=8, so m-4=5 for this range
    yval_lin.append(legendrepol(x,firstpoint,firstpoint+1))
    yval_glo.append(legendrepol(x,0,m-1))
    yval_cub.append(legendrepol(x,cubepoint,cubepoint+3))




# for x in xvalues:               
#     yvalues.append(legendrepol(x,firstpoint,firstpoint+numpoints-1))
    
#plt.plot(xin[0:m],yin[0:m],"o",label="Scattering Points")
#plt.plot(xvalues,yval_glo,color="orange", linewidth=1, linestyle="dashed", label="Global Interpolation")
#plt.plot(xvalues,yval_lin, color="green", linewidth=2, linestyle="solid", label="Linear Interpolation")
#plt.plot(xvalues,yval_cub, color="purple", linewidth=2, linestyle="dashed", label="Cubic Interpolation")
plt.plot(xvalues, yval_glo-1/(1+25*xvalues**2), linewidth=1.5, label="Gloabl Interpolation Error", color="red")
plt.plot(xvalues, yval_lin-1/(1+25*xvalues**2), linewidth=1.5, label="Linear Interpolation Error", color="green")
plt.plot(xvalues, yval_cub-1/(1+25*xvalues**2), linewidth=1.5, label="Cubic Interpolation Error", color="blue")
plt.legend(loc="lower center")
plt.xlabel("Energy (MeV)")
plt.ylabel("Cross Sectional Area")
plt.title("Lagrange Interpolation")
plt.axis([-1.1, 1.1, -0.2, 0.2])
plt.show()
