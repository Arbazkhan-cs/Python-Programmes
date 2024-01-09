num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
sums = num_1 + num_2
print("SUM: " + str(sums))


# String Functions
# num_1 is a str
num_1 = 'Python is for programing:)'
# For change the str into capital letter
print(num_1.upper())
# For finding the position of the str.
print(num_1.find('for'))
# For add any more words in the last of the str.
print(num_1.__add__(' :Arbaz Khan'))
# For replace any words in the str
print(num_1.replace('for', '4'))
# For searching the word is in the str, it will give you True or False
print('programing' in num_1)
print('arbaz' in num_1)


# Operations
# For Addition
print(10 + 10.5)
# For Subtraction
print(87 - 78)
# For Division
print(10 / 3)
# For reduce point in Division
print(10 // 3)
# For Multiplication
print(10 * 2)
# For power
print(2 ** 3)


# Comparison Operators
# For Less_Than
print(2 < 3)
# For Greater_Than
print(2 > 3)
# For Less_Than And Equal_Too
print(2 <= 3)
# For Greater_Than And Equal_Too
print(2 >= 3)
# For Equal_Too
print(2 == 3)
# For Not Equal_Too
print(2 != 3)


# Exercise
weight = float(input("Enter Your Weight? "))
KG_LB = input("Kg or Lbs(type k for Kg and type l for Lbs): ")
if KG_LB.upper() == 'l':
    To_Lbs = (weight / 0.45)
    print("Weight in Lbs: " + str(To_Lbs))
else:
    To_KG = (weight * 0.5)
    print("Weight in Kg: " + str(To_KG))
