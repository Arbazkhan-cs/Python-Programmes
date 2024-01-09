from functools import reduce


# Add function.
def add(*b): return sum(b)


result = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(result)

                                          # lamda function


# We can do this by lamda function.
add = lambda *b: sum(b)

result = add(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(result)
# _____________________________________________________________________________________________________________________


# Using filter(), map() and reduce() functions.
# num = [5, 7, 3, 8, 11, 4, 2, 9, 13, 4]

n = open('numbers', 'r')
x = n.read()


file = []
for i in range(len(x)):
    file.append(int(x[i]))


prime = list(filter(lambda b: b % 2 != 0 and b % 3 != 0, file))  # filter() is uses to filter the list and take element which we want.
print("Prime List:", prime)


sub = list(map(lambda b: b-2, prime))  # map() is uses to do arithmetic operation in the list for only one argument
print("Subtracting 2 in each element: ", sub)


add = reduce(lambda a, b: a+b, sub)  # reduce() is uses to get the value want we want after doing filter and mapping.
print("Sum:", add)
