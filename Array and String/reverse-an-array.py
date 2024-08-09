#Reverse an Array
#Description: Write a function that takes an array as input and returns the array in reverse order.

import numpy as np
#method1 by converting into list and use reverse fun
def rev_array(A):
    l=A.tolist()
    l.reverse()
    print(l)

#method 2 convert and access element by reverse
def rev_array2(A):
    l=A.tolist()
    print(l[::-1])

#method 3 by sorting the element
def rev_array3(A):
    A2=np.array([])
    c=0
    for i in range (0,len(A)):
        c=i-len(A)
        A2=np.append(A[c])
    print(A2)

A=np.array([1,2,5,6])
rev_array3(A)