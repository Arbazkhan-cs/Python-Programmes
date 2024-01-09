from numpy import *
arr = array([

            [1, 2, 3, 4],
            [4, 3, 2, 1]

            ])

print(arr)
print("Data Type       :", arr.dtype)
print("Dimension       :", arr.ndim)
print("Rows And Column : ", arr.shape)
print("ReShape         : ", arr.reshape(1, 8))


arr = input("ENTER THE FIRST ROW WITH SPACE: ").split()
arr1 = input("ENTER THE SECOND ROW WITH SPACE: ").split()
arr2 = input("ENTER THE THIRD ROW WITH SPACE: ").split()
New_matrix = matrix([
            arr,
            arr1,
            arr2
               ])
print(New_matrix)
