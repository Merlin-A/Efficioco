# Calcultor to calculate the effective time ratio
import time



def Calculator():
    a = 0
    b = 0
    week = []
    print("\n")
    print("Enter Your Useful Time")
    while True:

        z = int(input("\t->"))
        a = a + z
        if z == 0:
            break

    print("The useful time is:- ", a)
    print("\n")
    print("-"*20)

    print("\nEnter Your Unuseful Time")
    while True:

        y = int(input("\t->"))
        b = b + y

        if y == 0:
            break

    print("The unuseful time is:- ", b)

    comp = (int((a+b)/60)) + int((a+b) % 60)/1020
    add = int(a+b)
    e_t = float(a/add)
    print("\nThe total active time is", comp)
    print("\nTHE EFFECTIVE TIME RATIO IS:- ", e_t)

    if e_t >= 0.75:
        print("Keep Up The Good Work!!!!")
    else:
        print("\nYou're better than this.., Keep Going")

    choice = input("\nPress n to exit or press y to continue -> ")
    print("\n")

    if choice == "y":
        return Calculator()
    else:
        exit
            


        


Calculator()
