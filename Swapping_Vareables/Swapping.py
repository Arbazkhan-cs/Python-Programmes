# First Method For Swapping The Variables.
a = 4
b = 8
Swap = b
b = a
a = Swap
print(a)
print(b)

# Second Method For Swapping The Variables.
a = 4
b = 8
a = a + b
b = a - b
a = a - b
print(a)
print(b)

# Third Method For Swapping The Variables.
a = 4
b = 8
a, b = b, a
print(a)
print(b)
