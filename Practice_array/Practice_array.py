from array import *
# HOW TO USE ARRAY AND INPUT ARRAY OF UNICODE.
letter = input("Enter A letter what you want to print in an array: ")
array_l = array('u', letter)
print(array_l)
array_l.reverse()
print(array_l)
for i in range(len(array_l)):
    print(array_l[i])


#  HOW TO SORT THE ARRAY.
num = array('i', (9, 8, 7, 6, 5, 4, 3, 2, 1))
print(len(num))
for i in range(len(num)):
    for j in range(i, len(num)):
        if num[i] >= num[j]:
            num[i], num[j] = num[j], num[i]
            print(num)


# INPUT ARRAY BY USER IN INT FORMATE.
arr = array('i', [])

n = int(input("ENTER THE LENGTH OF THE ARRAY: "))

for i in range(n):
    ask = int(input("ENTER THE NEXT VALUE: "))
    arr.append(ask)

print(arr)


# DELETING THE ARRAY MANUALLY, AND SHIFTING THE ARRAY.
arr = array('i', [])
num = int(input("ENTER THE LENGTH OF THE ARRAY: "))

for i in range(num):
    value = int(input("Enter The Next Value: "))
    arr.append(value)
print(arr)

for i in range(num):
    for j in range(i, num):
        arr[i], arr[j] = arr[j], arr[i]
print(arr)


# QUESTION OF TWO SUM BY LEET CODE.
num = [3, 3, 5, 8]
target = 6
for i in range(len(num)):
    for j in range(i, len(num)):
        if i == j:
            continue
        if num[i] + num[j] == target:
            print(i, j)
