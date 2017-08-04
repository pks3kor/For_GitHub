"""
Author : Pankaj soni
"""


#~ NumPy's broadcasting rule relaxes this constraint when the arrays shapes meet certain constraints. The simplest
#~ broadcasting example occurs when an array and a scalar value are combined in an operation:
#~ The result is equivalent to the previous example where b was an array.  We can think of the scalar 
#~ being stretched during the arithmetic operation into an array with the same shape as The new elements in
#~ are simply copies of the original scalar.  The stretching analogy is only conceptual.  NumPy is smart enough to use the original scalar
#~ value without actually making copies, so that broadcasting operations are as memory and computationally efficient as possible.
#~ The code in the second example is more efficient than that in the first because broadcasting moves less memory around during the multiplication 
#~ (is a scalar rather than an array).
import numpy as np
a = np.arange(4)
b = np.array([2,2,2,2])
print a*b

c = 2
print a*c

#General Broadcasting Rules
#~ When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing dimensions, and
#~ works its way forward. Two dimensions are compatible when
#~ 1.  they are equal, or
#~ 2.  one of them is 1