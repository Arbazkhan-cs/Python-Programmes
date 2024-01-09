name = input("What Is Your Name? ")
print("Nice To See You "+name)


def percent(x, y):

    return x/y*100


while True:
    print("Let's Find Your Percentage:)")

    num1 = int(input("Total Number: "))
    num2 = int(input("Total Number You Get: "))
    print(num2, "/", num1, "*", 100, "=", percent(num2, num1))

    again = input("Do You Want To Do It Again(y/n)? ")
    if again == 'n':
        print("OK:)")
        break

print("Thanks For Using Me :)")
