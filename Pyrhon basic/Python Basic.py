Name = "Arbaz khan"
print(Name[::2])
print(Name[1:5:3])
# First Ratio Is For Where You Want To Start Print The Statement.
# Second Ratio Is For Where You Want To Stop It.
# Third Ratio Is For How Many Intervals Of Gape You Want To Print The Statement.


Name_1 = len(Name)  # Len Function For the length.
for i in range(Name_1):
    print(Name)

Good_boy = Name + " Is A Good Boy."  # Connecting Two Statement Together.
print(Good_boy)

A = "arbaz khan"
print(A.upper())  # Upper Function Is Used For Capitalisation Of Statement.
B = "ARBAZ KHAN"
print(B.lower())  # Lower Is Used For Convert Capital Into Lower.
C = "Arbaz Khan"
print(C.replace('Arbaz', 'Imran'))  # Replace A Word To Other Word.
D = "Arbaz Khan Arbaz Khan Arbaz Khan"
print(D.count('Arbaz'))  # Count Function Is Used For Count The Word In The Statement.
E = "Arbaz Khan"
print(E.find('Kh'))  # Find Function IS Used For Finding Word In The Statement.
print(E.find('I'))  # If The Word Is Not In The Statement It Displays -1.

print("I am a \ngood boy")  # \n Function Is For Printing The Statement In The Next Line.
print("I am a \rgood boy")  # \r Function Is For Deleting The Backward Statement.
print("I am a \tgood boy")  # \t Function Is For Use Tab Button In The Statement.

Tup = (1, 2, ("Arbaz", "Khan"), 3, 4, ("Good", (1, 2)))
print(Tup[2])  # For Find The Position Of Tuples Word.
print(Tup[5][1])  # For Find The Position Of Word In The Word.

Lists = [1, 2.5, 3, 4, "Arbaz Khan", 5, 6]
print(Lists[1])  # For Print What You Want To Print From The Lists.
print(Lists)
Lists.append('Good Boy')  # For Add More Things In The List.
print(Lists)
Lists[0] = 'Hello'  # For Add The Word Where you Want.
print(Lists)
del [Lists[5]]  # For Remove The Word What You Want To Remove It.
print(Lists)
Lists_1 = "A, B, C, D".split(",")  # For Separating The Words.
print(Lists + Lists_1)  # For Add Lists or variables.
