'''
Access Array Elements
Array indexing is the same as accessing an array element.
You can access an array element by referring to its index number.
The indexes in NumPy arrays start with 0, meaning that the first 
element has index 0, and the second has index 1 etc.
'''
import numpy as np 
array_1 = np.array([1,2,3,4,5,6,7,8,9])
#print 1
print(array_1[0])
#print 3
print(array_1[2])
# print 4+5
print(array_1[3]+array_1[4])

#------------2D array--------------
'''
To access elements from 2-D arrays we can use comma separated integers 
representing the dimension and the index of the element.
----
Think of 2-D arrays like a table with rows and columns, where the dimension 
represents the row and the index represents the column.
'''
array_2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print 8
print(array_2[1,2])
#print 4
print(array_2[0,3])
#print 10 (Negative)
print(array_2[1,-1])
#------------3D array--------------

array_3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#print 6
print(array_3[0,1,2])

'''
[0,1,2] --> [0,.,.]--> [1,2,3],[4,5,6] , [.,.,.],[.,.,.]
[0,1,2] --> [.,1,.]--> [.,.,.],[4,5,6] , [.,.,.],[.,.,.]
[0,1,2] --> [.,.,2]--> [.,.,.],[.,.,6] , [.,.,.],[.,.,.]

`arr[0, 1, 2]` returns `6`.
Think of the 3D array as boxes inside boxes.

- **First number `0`** → opens the first big box.
  Inside it we have: `[[1,2,3], [4,5,6]]`
- **Second number `1`** → inside that box, picks the second small box.
  Inside it we have: `[4, 5, 6]`
- **Third number `2`** → inside that small box, picks the third number.
  The numbers are `4`, `5`, `6`, so the third one is `6`.
So step by step we go deeper: **big box → small box → number**.
'''