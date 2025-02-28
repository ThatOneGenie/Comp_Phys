#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:50:56 2025

@author: genie
"""
from hermite import herm
import numpy as np
import math
from scipy import constants as scp
from scipy import integrate

class Qho:
    def __init__(self,mass,omega,xvals):
        self.omega = omega
        self.xvals = xvals
        try:
            if mass > 0:
                self.mass = mass
        except:
            print("Mass cannot be negative. Assuming absolute value for mass.")
            self.mass = np.abs(mass)
        
    def wavefunction(n,x):
        norm = ((Qho.mass*Qho.omega)/(np.pi*scp.hbar))**0.25
        beta = np.sqrt((Qho.mass*Qho.omega)/scp.hbar)
        bx = beta*x
        Hn = herm(n, bx)
        psi_n = norm * np.exp(-((beta**2)*(x**2))/2) * Hn
        return psi_n
    
    def wave_simp(n,x):
        norm = 1/(2**n * math.factorial(n) * np.sqrt(np.pi)) 
        #Now simply calculate wavefunction using definition
        print(herm(n,x))
        psi_n = norm * herm(n,x) * np.exp(-x**2/2) #importing from hermite.py
        return psi_n
    
    def prob_dens(n,xvals):
        psi_n = Qho.wavefunction(n, xvals)
        prob_dens = (np.abs(psi_n))**2
        return prob_dens
    
    def expect(n,xvals):
        psi_n = Qho.prob_dens(n, xvals)
        exp_val = integrate.simpson(xvals*psi_n, x=xvals)
        exp_val2 = integrate.simpson((xvals**2)*psi_n, x=xvals)
        stand_dev = np.sqrt(exp_val2-exp_val**2)
        return exp_val, stand_dev
    
    
        
        
        
                                


    
