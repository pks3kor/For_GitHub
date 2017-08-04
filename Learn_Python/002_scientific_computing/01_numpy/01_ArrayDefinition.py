"""
Author : Pankaj soni
"""

import numpy as np

tmp = np.arange(6)
# tmp = np.arange(6)
print tmp.shape
print tmp.ndim
print tmp.dtype
print tmp.itemsize
print tmp.size
print type(tmp)

tmp = np.arange(6).reshape(3,2)
# tmp = np.arange(6)
print tmp.shape
print tmp.ndim
print tmp.dtype
print tmp.itemsize
print tmp.size
print type(tmp)