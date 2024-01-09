name = input("What Is Your Name: ")
print("Nice To See You " + name)

square = input("Do you Want To Make The Square(y/n): ")
if square == 'y':
    n = int(input("Enter The Number Of Rows For Making The Square: "))
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
else:
    print("Ok :)")


RT = input("Do You Want To Make Right Triangle(y/n):  ")
if RT == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i + 1):
            print("$", end=" ")
        print()
else:
    print("Ok :)")


LT = input("Do You Want To Make The Left Triangle(y/n): ")
if LT == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i + 1):
            print("&", end=" ")
        print()
else:
    print("Ok :)")


ILT = input("Do you Want To Make The Inverse Of Left Triangle(y/n): ")
if ILT == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print("%", end=" ")
        print()
else:
    print("Ok :)")


Triangle = input("Do You Want To Make The Triangle(y/n):")
if Triangle == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print("@", end=" ")
        for j in range(i + 1):
            print("@", end=" ")
        print()
else:
    print("Ok :)")


IRT = input("Do You Want To Make Inverse of Right Triangle(y/n): ")
if IRT == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i, n):
            print("#", end=" ")
        print()
else:
    print("Ok :)")


IT = input("Do You Want To Make The Inverse Triangle(y/n): ")
if IT == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print("=", end=" ")
        for j in range(i, n - 1):
            print("=", end=" ")
        print()
else:
    print("Ok :)")


TLW = input("Do You Want To Make The Triangle On Left Wall(y/n): ")
if TLW == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i):
            print("?", end=" ")
        print()
    for i in range(n):
        for j in range(i, n):
            print("?", end=" ")
        print()
else:
    print("Ok :)")


TRW = input("Do You Want To Make The Triangle On Right Wall(y/n): ")
if TRW == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print("!", end=" ")
        print()
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(i, n):
            print("!", end=" ")
        print()
else:
    print("Ok :)")


Diamond = input("Do You Want To Make The Diamond(y/n): ")
if Diamond == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n - 1):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print("@", end=" ")
        for j in range(i + 1):
            print("@", end=" ")
        print()
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print("=", end=" ")
        for j in range(i, n - 1):
            print("=", end=" ")
        print()
else:
    print("Ok :)")


Butterfly = input("Do You Want To Make A Butterfly(y/n): ")
if Butterfly == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i):
            print("?", end=" ")

        for j in range(i, n - 1):
            print(" ", end=" ")
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i + 1):
            print("?", end=" ")
        print()
    for i in range(n):
        for j in range(i, n):
            print("?", end=" ")
        for j in range(i):
            print(" ", end=" ")
        for j in range(i):
            print(" ", end=" ")
        for j in range(i, n):
            print("?", end=" ")
        print()
else:
    print("Ok :)")


Timer = input("Do You Want To Make A Timer(y/n): ")
if Timer == 'y':
    n = int(input("Enter The Number Of Rows: "))
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(i, n - 1):
            print("$", end=" ")
        for j in range(i, n):
            print("$", end=" ")
        for j in range(i + 1):
            print(" ", end=" ")
        print()
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print("$", end=" ")
        for j in range(i + 1):
            print("$", end=" ")
        for j in range(i, n):
            print(" ", end=" ")
        print()
else:
    print("Ok :)")
print("Thanks For Using Me :)")
