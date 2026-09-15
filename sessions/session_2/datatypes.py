#Data Types in Python :
'''
strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
'''
#Data Types in numpy :
'''
NumPy has some extra data types,
and refer to data types with one character,
like i for integers, u for unsigned integers etc.
--------------------------------------------------------------
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
'''
#The NumPy array object has a property called dtype that returns the data type of the array
import numpy as np

a_array = np.array([1,2,3,4,5])
b_array = np.array(["Hello","World"])
print(a_array.dtype)
print(b_array.dtype)

''' Next update at 16 sep 
    add Doc->step_3.md - complete datatypes.py
'''