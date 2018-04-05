# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from scipy import *

# 
def ctrapezoidal(f, a, b, n):
    """Estimates the integral of f from a to b in n steps
    using the composite trapezoidal rule.

    Parameters
    ----------
    f : function taking one integer argument
        the function to be integrated
    a : float
        start point
    b : float
        end point
    n : int
        number of steps, must be greater than zero

    Returns
    -------
    float
        the approximated value of the integral

    Raises
    ------
    OtherError
        when an other error
    """
    
    assert n > 0, 'Must have positive number of steps'
    
    # Complicated one-liner
    # notes that it goes to n-1
    s = [f( a + i/n*(b-a) ) for i in range[1, n] ]
    h = (b-a)/n
    return 0.5*h*( f(a) + f(b) ) + h*sum(s)
    
#
def cloop(TOLERANCE):
    assert TOLERANCE > 0, "Tolerance must be positive"
    
    Ih = ctrapezoidal(f,a,b,n)
