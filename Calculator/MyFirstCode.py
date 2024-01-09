name = input("What Is Your Name: ")
print("Nice To See You " + name)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def dive(x, y):
    return x / y


def power(x, y):
    return x**y


while True:
    print("let's do calculation")

    print("Select a operation:")
    print("1).Addition")
    print("2).Subtraction")
    print("3).Multiplication")
    print("4).Division")
    print("5).Power")

    Choice = input("Select a operation(1/2/3/4/5): ")

    if Choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if Choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif Choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif Choice == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif Choice == '4':
            print(num1, "/", num2, "=", dive(num1, num2))

        elif Choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))

        again = input("Do you want to do again(yes/no)? ")
        if again == 'yes' or again == 'y':
            continue

        elif again == 'no' or again == 'n':
            break

        else:
            print("Invalid input!!")
            break

    else:
        print("Ok :)")
        print("invalid input!!!")

print("Thanks For Using Me:)")
