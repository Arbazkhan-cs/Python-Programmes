# Dictionary
my_dict = {"Name": "Arbaz", "Age": 17, "Class": 12}  # For Making The Dictionary.
print(my_dict)

value = my_dict["Age"]  # Finding The Element By Key.
print(value)

my_dict["City"] = "New Delhi"  # For Adding More Key Word.
print(my_dict)

del my_dict["Age"]  # For Deleting The Key Word.
print(my_dict)

my_dict.popitem()  # For Deleting The Last Key Word.
print(my_dict)

my_dict["Age"] = 17
my_dict["City"] = "New Delhi"
print(my_dict)

if "City" in my_dict:  # For Seeing The Key Word In The List
    print(True, ":", my_dict["City"])
else:
    print(False)

# Or We Can Use This Method For Seeing The Key Word.

try:
    print(my_dict["City"])
except:
    print("Error")


for key in my_dict.keys():  # For Printing All The Keys In The List.
    print(key)
for value in my_dict.values():  # For Printing All The Values In The List.
    print(value)
for key, value in my_dict.items():  # For Printing The Key And The Value Together.
    print(key, value)

print(my_dict)
new_dict = my_dict
# For Making Another Dictionary Like Previous Dictionary.
# If We Change New_Dict It Will Automatically Change The Old Dictionary.
new_dict["Email"] = "imran9953532472@gamil.com"
print(new_dict)
print(my_dict)

new_dict = my_dict.copy()
# For Making Another Dictionary Like Previous Dictionary.
# If We Change New Dictionary It Will Not Change Old Dictionary.
new_dict["Number"] = 9953532472
print(new_dict)
print(my_dict)


dict_1 = {"name":"Arbaz", "age":17, "class":12}
print(dict_1)
dict_2 = dict_1.copy()
dict_2["email"] = "imran9953532472@gmail.com"
print(dict_2)
dict_1.update(dict_2)  # It Will Add The Thing Which Is Not In The Fist Dictionary From Second Dictionary.
print(dict_1)











