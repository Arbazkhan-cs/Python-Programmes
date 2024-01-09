"""# Exercise 6.5
texts = "X-DSPAM-Confidence:      0.8475"
texts_1 = float(texts[texts.find(':')+1:].strip())
print(texts_1)
"""
"""
# Exercise 7.2
fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("The File Is Not Excceds:(")
    quit()

total = 0
count = 0
for i in fhand:
    if i.startswith('X-DSPAM-Confidence:'):
        x = i[20:28]
        y = float(x)
        count += 1
        total += y
print("Average spam confidence:",total/count)"""

"""
f_name = open('edx_file_oppening.PNG','rb')
f_name_copy = open('copy','w')

f_name_copy.write("HELLO\nWORLD\nI AM ARBAZ KHAN.\nI AM 17 YEARS OLD.")"""


# Tuples

dic = {'a': 34, 'c': 91, 'b': 46}

lst = sorted(dic.items())  # This only sort the keys.
print(lst)

lst = sorted([(v,k) for(k,v) in dic.items()])  # This only sort the Values.
print(lst)

# Sorting The above by Manually.

lst = []
for (k, v) in dic.items():
    new_tup = (v, k)
    lst.append(new_tup)

lst = sorted(lst)
print(lst)
