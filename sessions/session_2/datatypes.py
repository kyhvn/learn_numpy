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
b_array = np.array(["Hello","World!"])
print(a_array.dtype)
print(b_array.dtype)

'''We use the array() function to create arrays,
 this function can take an optional argument: (dtype) 
 that allows us to define the expected data type of the array elements
'''
c_array=np.array([1,2,3,4,5],dtype='S')
print(c_array)
print(c_array.dtype)

#For i, u, f, S and U we can define size as well.
# Create an array with data type 4 bytes integer:
array_4byte = np.array([1,2,3,4,5],dtype='i4')
array_string = np.array([1,2,3,4,5],dtype='S4')
print(array_4byte)
print(array_4byte.dtype)

print(array_string.dtype,array_string)

#ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.
#If a type is given in which elements can't be casted then NumPy will raise a ValueError.
print("\n-----------What if a Value Can Not Be Converted?-----------\n")
def ValueError_test():
    try:
        arr = np.array(['x', 2, 5], dtype='i')
        return arr
    except ValueError:
        return "ValueError"


def ValueError_test_true():
    try:
        arr = np.array(['4', 2, 5], dtype='i')
        return "this is ok", arr
    except ValueError:
        return "ValueError"

print(ValueError_test())
print(ValueError_test_true())


'''
The simplest way to change the data type of an existing array is to use astype().
It creates a new copy of the array with the specified data type. For example,
use astype('f') or astype(float) for float, and astype('i') or astype(int) for integer.
'''
print("\n----------Converting Data Type on Existing Arrays---------\n")
first_array = np.array([1.1, 2.1, 3.4, 4.5, 5.8])

def change_with_i(first_array):
    # convert :
    new_array = first_array.astype('i')
    # export:
    print(f"first_array: {first_array} : {first_array.dtype}\nnew_array: {new_array} : {new_array.dtype}")

def change_with_int(first_array):
    # convert :
    new_array = first_array.astype(int)
    # export:
    print(f"first_array: {first_array} : {first_array.dtype}\nnew_array: {new_array} : {new_array.dtype}")


print("change with (i): ")
change_with_i(first_array)
print("change with int : ")

change_with_int(first_array)

#Change data type from integer to boolean:

first_array[1] = 0

def change_with_boolean(first_array):
    new_array = first_array.astype(bool) # x==0 = false - 0<x = true
    print(f"first_array: {first_array} : {first_array.dtype} new_array: {new_array} : {new_array.dtype}\n")

print("change with (bool): ")
change_with_boolean(first_array)