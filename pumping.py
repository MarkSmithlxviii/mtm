# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 05:51:29 2017

@author: msmith
"""

from math import pi
from math import sqrt

import numpy as np
import pandas as pd


def orificeFlow(orificeDiam, head):
    """ 
    The flow through an orrifice is given by:
        
        Q = CA sqrt(2gh)
    
    where:
        Q is flow in m/s
        C is the orifice Coefficient (unitless)
        A is the area of the orifice (m^2)
        g is the acceleration due to gravity 9.81 m/s/s, and 
        h is the height of water above the centre of the orifice (m).
        
    Inputs to the function are the orrifice diameter and the height
    of water above the orifice centre.
    
    Output is the flow through the orifice in m^3/s
    """
    c = 0.61
    g = 9.81
    
    area = pi * (orificeDiam/2)^2
    
    flow = c * area * sqrt(2 * g * head)
    return flow

def incrementalHeadLoss(previousPumpFlow, num90, num45, numCheckValve, 
                      idFirstPipe, idSecondPipe):
    """
    Incremental head losses will be calculated calculated based on flow 
    coefficients for the various inline sources of friction.
    
    
    """

        