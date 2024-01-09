import random as r


def guess_the_number():

    nums = r.randrange(0, 1000, 1)
    count = 0
    print("If You Don't Want to become a Plumber")
    print("Then, Guess The Number!!!")
    print("Range: (0, 1000) \n")

    while True:
        try:
            ask = int(input("Enter the number: "))
        except:
            print("Enter a Valid Number!!!")
            continue

        count += 1

        if ask == nums:
            print("You Found It:) In", count, "Times \n")
            break

        elif ask > nums:
            print("The Number Is Smaller!")

        elif ask < nums:
            print("The Number Is Greater!")

    if count > 12:
        print("You Are A Plumber:(")
    else:
        print("You Are Not A Plumber:)")

    print("Thanks For Coming Here")
