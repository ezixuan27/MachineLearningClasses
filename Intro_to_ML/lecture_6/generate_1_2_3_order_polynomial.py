#!/usr/bin/env python

import numpy as np
import wplotlib
from wplotlib import *

x = np.arange(-3, 3, 0.1)
y = 2*x + 2 + 0.5*np.random.randn(len(x))
y2 = 2*x*x + x +  2 + 0.5*np.random.randn(len(x))
y3 = x*x*x + x +  2 + 0.8*np.random.randn(len(x))

wplotlib.scatter(x, y, '', 'X axis', 'Y axis', ticker_fontsize=12, xticker_rotate=90)	
wplotlib.scatter(x, y2, '', 'X axis', 'Y axis', ticker_fontsize=12, xticker_rotate=90)	
wplotlib.scatter(x, y3, '', 'X axis', 'Y axis', ticker_fontsize=12, xticker_rotate=90)	
#
