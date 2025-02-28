#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:54:20 2025

@author: genie
"""

import numpy as np
from quantum import Qho
import matplotlib.pyplot as plt
from scipy import constants as scp

def main():
    Qho.mass = (9.109*10**-31)      # Mass of electron
    Qho.omega = 2*np.pi
    xvals = np.linspace(-1,1,200)
    nmax = 10
    for n in range(nmax+1):
        return Qho.prob_dens(n, xvals)

Qho.mass = scp.m_e
      # Mass of electron
Qho.omega = (2*np.pi)/25
xvals = np.linspace(-1,1,200)
n = 0
psi_n = Qho.prob_dens(n, xvals)
plt.plot(xvals, psi_n)
    
    
if __name__ == "__main__":
    main()