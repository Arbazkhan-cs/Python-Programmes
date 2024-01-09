list_1 = []
list_2 = []


num_1 = int(input("ENTER THE LENGTH OF THE FIRST LIST: "))
for i in range(num_1):
    l_1 = int(input("ENTER THE NEXT NUMBER: "))
    list_1.append(l_1)
print("FIRST LIST:", list_1)


num_2 = int(input("ENTER THE LENGTH OF THE SECOND LIST: "))
for i in range(num_2):
    l_2 = int(input("ENTER THE NEXT NUMBER: "))
    list_2.append(l_2)
print("SECOND LIST:", list_2)


new_list = list_1 + list_2
new_list.sort()
print("NEW LIST:", new_list)
