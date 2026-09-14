'''
Hi! 
I want to learn NumPy,
so I created this repository.
I hope to complete it fully and help you 
learn this library as well.
My source this time is "https://www.w3schools.com"
and we’ll go through this journey together
'''
import numpy  # To import it, we need to install NumPy ==> pip install numpy

arr = numpy.array([1,2,3,4,5])
print(arr,type(arr)) # a object from calss numpy.ndarray


#NumPy is usually imported under the np alias.
import numpy as np
arr2 = np.array((1,2,3,4,5))
print(arr2,type(arr2))

#Checking NumPy Version
# The version string is stored under (__version__) attribute
print(f"numpy version : {np.__version__}\n")

'''
To create an ndarray, we can pass a list, tuple or any array-like 
object into the array() method, and it will be converted into an ndarray
----------------------------------------------------------------------
Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).
nested array: are arrays that have arrays as their elements.
'''

#0D arrays
array_0D = np.array(20)
#1D arrays
array_1D=np.array([20,30,40])

#2D arrays 
# An array that has 1-D arrays as its elements is called a 2-D array
# These are often used to represent matrix or 2nd order tensors.
array_2D = np.array([[1,2,3],[4,5,6]])
print('2D array:\n',array_2D,)

#3D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
array_3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
'''
([  [a1] , [a2]     ],    [    [b1] , [b2]   ])
'''
print('3Darray:\n',array_3D)

# NumPy Arrays provides the " ndim " attribute that returns an integer 
# that tells us how many dimensions the array have.
print(f"dimension number: {array_0D.ndim}")
print(f"dimension number: {array_1D.ndim}")
print(f"dimension number: {array_2D.ndim}")
print(f"dimension number: {array_3D.ndim}")
#When the array is created, you can define the number of dimensions by using the ( ndmin ) argument
x_array = np.array([1,2,3,4],ndmin=3)
print(f"{x_array}\ndimensions:{x_array.ndim}")

'''
In this array the innermost dimension (5th dim) has 4 elements,
the 4th dim has 1 element that is the vector,
the 3rd dim has 1 element that is the matrix with the vector,
the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
'''

