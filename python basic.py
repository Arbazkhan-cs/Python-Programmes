print("Arbaz khan")

# List

# List is the one of the best methods to storage the data as it is mutable and works in any data type.
x = [25, "Hello", 9.3]
print(x)
print(x[0])  # Slicing.
print(x[-1])
print(x[1])
print(len(x))  # For Checking The Length Of List.
print(type(x))  # It uses to know the data type of the variable.

y = ["World", 19, 0.5]

z = x + y  # Adding them adding in z.
print(z)
z = [x, y]  # Adding them and creating List inside a List.
print(z)

# Using In Built Function In List.
x.append(821)
print(x)
x.pop(1)  # It is use for removing the object by there index number.
print(x)
print(x.index(821))  # To find the index number.
x.remove(25)  # It uses for removing the object by there element name when we don't want to use pop function.
print(x)
x.append("Hello")  # It Uses To Add The Objects.
print(x)
x.reverse()  # It uses for reversing the List.
print(x)
x.clear()  # It uses to empty the list.
print(x)
z = [10, 5, 2, 9, 4, 1]
z.sort()  # It Uses to arrange only int or float in ascending order.
print(z)
z.insert(1, "Hello")  # It Uses to add the object at any index number.
print(z)
z.extend([11, 14, 15])  # It uses to add multiple values in the List.
print(z)
del z[2]  # It is also uses for delete the element by its index number with slicing.
print(z)
del z[4:7]  # It will remove all the element which index number is 4 to 6.
print(z)
z.remove("Hello")
print(min(z))  # It uses to find the minimum number in the list.
print(max(z))  # It uses to find the maximum number in teh list.
print(sum(z))  # It uses to add all the numbers in the list.
# __________________________________________________________________________________________________________________________________________________________


# Tuple

# Tuple is also uses to store the data, but it is immutable, and it can work in any data type.
num = (1, 2, 2.6, "World")
print(num)
print(num[1:3])  # Slicing
print(type(num))  # Data type

num_2 = (1, 2, 3, 4, 3)
num_3 = num + num_2  # We can Add to tuple
print(num_3)

# Using In Built Function Of Tuple.
print(num.index("World"))  # It uses to find the index number.
print(num_2.count(3))  # It uses to find how many times a number is in data.
# ___________________________________________________________________________________________________________________________________________________________


# Set

# Set is also a one of the best method to store the data as it does not have any specific index number for the Elements.
S = {1, 2, 'Hello', 9.5, 9.5}
print(S)
print(type(S))

# In Built Functions Of The Set.
""" add(...)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |
 |  clear(...)
 |      Remove all elements from this set.
 |
 |  copy(...)
 |      Return a shallow copy of a set.
 |
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |
 |      (i.e. all elements that are in this set but not the others.)
 |
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |
 |      If the element is not a member, do nothing.
 |
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |
 |      (i.e. all elements that are in both sets.)
 |
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |
 |  issubset(...)
 |      Report whether another set contains this set.
 |
 |  issuperset(...)
 |      Report whether this set contains another set.
 |
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |
 |      (i.e. all elements that are in exactly one of the sets.)
 |
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |
 |  union(...)
 |      Return the union of sets as a new set.
 |
 |      (i.e. all elements that are in either set.)
 |
 |  update(...)
 |      Update a set with the union of itself and others.
 """
# ___________________________________________________________________________________________________________________________________________________________


# Dictionary

ph_num = {"Saif Ali Khan": 9870142462, "Arbaz Khan": 9953532472, "Imran Khan": 8700110442}
print(ph_num)
print(ph_num["Arbaz Khan"])

ph_num["Papa Jio"] = 9818754571
print(ph_num)

# In Built Functions Of Dictionary
"""
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |
 |      If key is not found, default is returned if given, otherwise KeyError is raised
 |
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 """

# We can also integrate to list into dictionary.
name = ["Arbaz", "Imran", "Saif"]
lang = ["Python", "Java", "Linux"]
data = dict(zip(name, lang))
print(data)

# We can Have list in dictionary as well as dictionary in dictionary.
data = {'name': 'Arbaz', 'class': 12, 'prog': ['python', 'Java'], 'bro': {'Saif': 'Linux', 'Imran': 'Java'}}
print(data)
print(data['prog'][0])
print(data['bro']['Imran'])

print(type(data))  # Data Type.

# __________________________________________________________________________________________________________________________________________________

# Address Of The Variable

''' If the two variable have same data, then both have same addresses. '''
x = 10
y = 63
print(id(x))  # To see the address of the variable
print(id(y))

y = x  # Here we assigned both data same which is 10.
print(id(y))
print(id(x))
# So, as they have same data they got same addresses.
# ________________________________________________________________________________________________________________________________________________________

# Bitwise Operators

a, b = 15, 12
x = (a // 4 + b ** 3) < 2000 and (b % 4 != 0)
print(x)
print(~18)  # It is the ""compliment"" operator.
print(18 & 23)  # It is ""and"" operator.
print(16 | 29)  # It is ""or"" operator.
print(12 ^ 13)  # It is ""XOR"" operator.
print(15 << 2)  # It is ""Left Shift"" operator.
print(15 >> 2)  # It is ""Right Shift"" operator.
# ________________________________________________________________________________________________________________________________________________________

# Finding the cube.
from math import pow
num = int(input("Enter the number for cube: "))
print(int(pow(num, 3)))


# Finding the cube by manually.
def cube(x):
    y = 3
    return x**y


num = int(input("Enter A NUMBER: "))
result = cube(num)
print(result)


# For finding odd and even number
num = int(input("Enter A NUMBER: "))
if num % 2 == 0:
    print("IT IS AN EVEN NUMBER! ")

elif num % 2 != 0:
    print("IT IS AN ODD NUMBER! ")

else:
    print("INVALID INPUT!!!")


# Finding the greatest number
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

if x > y and x > z:
    print(x)

elif y > x and y > z:
    print(y)

elif z > x and z > y:
    print(z)


# Write a code to print all the values from 1to 100.
# Skip the numbers which are divisible by 3 or 5.
i = 1

while i <= 100:
    if i % 3 == 0 or i % 5 == 0:
        i += 1
        continue

    else:
        print(i)
    i += 1


# Pattern
i = 1
while i <= 5:
    print("# ", end=" ")
    j = 1
    while j <= 4:
        print("# ", end=" ")
        j += 1
    i += 1
    print()


# Finding the perfect sqrt between 1 and 500.
import math as m
for i in range(1, 500):
    j = m.pow(i, 2)

    if j > 500:
        break

    print(j)


# Finding Prime Number
while True:
    num = int(input("Enter A Number: "))

    if num % 2 != 0 and num % 3 != 0:
        print("It is a prime number")

    elif num == 2 or num == 3:
        print("It is a prime number")

    else:
        print("It is not a prime number")

    conti = input("Do You Want To Continue(yes or y/no or n): ")

    if conti == 'no' or conti == 'n':
        break


print("Bye")


# Three ways to make a left triange.

# 1). Way
for i in range(1,6):
    print("*",end=" ")
    for j in range(1,i):
        print("#",end=" ")

    print()

# 2). Way
for i in range(5):
    print(" # "*(i+1),end=" ")
    print()

# 3). Way
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")

    print()


# Three Ways to make left triangle upside down

# 1). Way
for i in range(1,6):
    print("*",end=" ")
    for j in range(5,i,-1):
        print("#",end=" ")

    print()

# 2). Way
for i in range(5,1,-1):
    print(" # "*(i-1),end=" ")
    print()

# 3). Way
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()


# Exercise:
# 1).
for i in range(4):
    for j in range(1,5-i):
        print(j+i,end=" ")
    print()

# 2).
for i in range(4):
    for j in range(i+1):
        print(chr(65 + j),end=" ")

    for j in range(i,3):
        print(chr(80+j),end = " ")

    print()
# _______________________________________________________________________________________________________________________________________________________

# ARRAY
from array import *
num = array('i', [1, 2, 3, 4, 5, 6, 7]) # It is an array with int data type.

new_num = array(num.typecode, [a for a in num])  # Creating same array by num array.

print(num)
print(new_num)

print(num.buffer_info())  # It is used to see the address of the array and its length.

# Input in array
arr = array('i', [])
num = int(input("Enter The Length Of The Array: "))
for i in range(num):
    x = int(input("Enter The Number"))
    arr.append(x)

print(arr)

# Sorting of array
num = array('i', [9, 4, 2, 7, 1, 8])
count = 0
for i in range(len(num)):

    for j in range(i, len(num)):

        if num[i] > num[j]:

            num[i], num[j] = num[j], num[i]

            print(num)

def fact(x):
    for i in range(1, x):
        x = x * i

    return x


print(fact(4))


# Finding Index Number Of The Array.
from array import *
arr = array("i", [9, 8, 4, 6, 2, 3, 1])

x = int(input("Enter the number for there index number: "))
print(arr.index(x))  # Using In-built Function

for i in range(len(arr)):  # Manually
    if x == arr[i]:
        print(i)
        break

