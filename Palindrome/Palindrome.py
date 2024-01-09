num = int(input("Enter the number: "))

New_num = num

rev = 0

while num > 0:
    last_num = num % 10
    num = num//10
    rev = rev * 10 + last_num

print(rev)

if New_num == rev:
    print(True)

else:
    print(False)


# Reverse of int PALINDROME
x = 11211
y = [str(x)]

low = 0
high = -1

while True:
    try:
        if y[0][low] == y[0][high]:
            low += 1
            high -= 1
            continue

        else:
            print(False)
            break

    except:
        print(True)
        break
