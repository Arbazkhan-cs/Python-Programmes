from numpy import *

arr = array([9, 6, 3, 7, 2, 8, 1])

print(arr)

# Adding 5 in each element in array by manually.
for i in range(len(arr)):
    arr[i] = arr[i] + 5

print(arr)

# Adding 5 in each element in array by inbuilt function.
arr_1 = array([1, 2, 3, 4, 5, 6, 7])

arr_1 = arr_1 + 5

print(arr_1)

# Reversing the array.
rev = array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(rev)

for i in range(len(rev)):

    for j in range(i):
        rev[i], rev[j] = rev[j], rev[i]

print(rev)

# Finding the maximum value in array.
# 1). Method
x = array([1, 3, 2, 7, 3, 9, 11, 14])

count = 0

for i in range(len(x)):

    for j in range(1, len(x)):

        count += 1

        if x[i] < x[j]:
            break

    else:
        print("Maximum value in array:", x[i], count)
        break

# 2). Method
x = array([1, 3, 2, 7, 3, 9, 11, 14])

y = 0
count = 0

for i in range(len(x)):

    count += 1

    if y < x[i]:
        y = x[i]

print(y, count)

# ___________________________________________________________________________________________________________________________________________________
lis = []
lis1 = []
lis2 = []

n = int(input("Enter the length of the matrix: "))

for i in range(n):
    for j in range(n):

        n1 = int(input("enter the next value: "))

        if i == 0:
            lis.append(n1)

        elif i == 1:
            lis1.append(n1)

        elif i == 2:
            lis2.append(n1)

        else:
            break

# print(lis,lis1,lis2)
x = array([lis, lis1, lis2])

print(x)


# ____________________________________________________________________________________________________________________________________________________

def add(**b):  # If we don't know the parameters.  # If we want to make parameters we will use ( ** ) by key and value.
    a = 0

    for i in b:
        a += i

    return a


print("Sum: ", add(a=1, b=7, c=2, d=8, e=0))


# _______________________________________________________________________________________________________________________________________________________

# Finding factorial by recursion.


def fact(x):
    if x == 1:
        return 1

    return x * fact(x - 1)


x = int(input("Enter The Number: "))

print("Factorial is:", fact(x))

# ________________________________________________________________________________________________________________________________________
# Finding Index number by recursion.
c = 0

y = int(input("enter the number: "))


def index(x):
    global c

    try:
        if y == x[c]:
            return c

    except:

        return 'Number is not in the list!!!', IndexError()

    c += 1

    return index(x)


z = [6, 3, 8, 1, 9, 4]

print("Index Number: ", index(z))
