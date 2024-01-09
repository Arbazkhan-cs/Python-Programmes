
def multiply(n):
    f = 1
    for i in range(1, n + 1):
        f = f*i
    return f


while True:
    x = int(input("Enter A Number For Factorial: "))

    result = multiply(x)

    print(result)

    again = input("Do You Want To Do It Again?(y/n)")
    if again == 'n':
        print("Ok :)")
        break
print("Thanks For Using Me :)")
