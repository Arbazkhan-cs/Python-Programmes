print("Now, let's do odd and even!!!")

while True:
    for i in range(1):
        num = int(input("Enter a number: "))

        if (num % 2) == 1:
            print("odd")

        else:
            print("even")
    again = input("Do you want to do again(yes/no)? ")
    if again == 'no' or again == 'n':
        break

print("Thanks For Using Me: ")
