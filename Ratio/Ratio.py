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
        print("\nYou're better than this..., Keep Going")

    choice = input("\nPress n to exit or press y to continue -> ")
    print("\n")

    if choice == "y":
        return Calculator()
    else:
        ask = (input("Do you want the Poem -> "))

        if ask == "y" or ask == "yes":
            print("\n")
            speed = float(input("Enter your preferred speed (recommended 4.3) -> "))   
            print("\n") 

            print("It's doing your job the best you can \nAnd being just to your fellow man;")
            time.sleep(speed)
            print("\n")

            print(
            "It's making money—but keeping friends \nAnd being true to your aims and ends;")
            time.sleep(speed)
            print("\n")

            print(
            "It's figuring how and learning why \nAnd looking forward and thinking high")
            time.sleep(speed)
            print("\n")
            

            print(
            "And dreaming a little and doing much \nIt's keeping always in closest touch")
                  
            time.sleep(speed)
            print("\n")


            print(
            "With what is finest in word and deed; \nIt's being thorough, yet making speed;")
            time.sleep(speed)
            print("\n")


            print(
            "It's daring blithely the field of chance \nWhile making labor a brave romance;")
            time.sleep(speed)
            print("\n")


            print("It's going onward despite defeat \nAnd fighting staunchly, but keeping sweet;")
            time.sleep(speed)
            print("\n")


            print("It's being clean and it's playing fair; \nIt's laughing lightly at Dame Despair;")
            time.sleep(speed)
            print("\n")


            print("It's looking up at the stars above \nAnd drinking deeply of life and love.")
            time.sleep(speed)
            print("\n")


            print("It's struggling on with the will to win \nBut taking loss with a cheerful grin;")
            time.sleep(speed)
            print("\n")


            print ("It's sharing sorrow and work and mirth \nAnd making better this good old earth;")
            time.sleep(speed)
            print("\n")


            print("It's serving, striving through strain and stress; \nIt's doing your noblest—that's Success!")

            print("\n")
            if input("Press Any Button to Quit") == " ":
                time.sleep(1.1)
                print("\n Thanks for Using!")

                exit
            else:
                exit


        exit


Calculator()
