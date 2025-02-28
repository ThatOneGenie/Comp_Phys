#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:52:28 2025

@author: genie
"""

import numpy as np

def herm(n,x):
    He_0 = np.ones_like(x)
    He_1 = 2*x
    if n == 0:
        H_n = He_0
    elif n == 1:
        H_n = He_1
    else:
        Hn2 = He_0
        Hn1 = He_1
        for i in range(2,n+1):
            H_n = 2*x*Hn1 - 2*(i-1)*Hn2
            Hn2 = Hn1
            Hn1 = H_n
    return H_n 
    