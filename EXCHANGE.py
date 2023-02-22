import sys

dollar = 1.36
euro = 1.20
HKD = 10.52
TL = 18.21


class Conversion:

    def __init__(self):
        pass

    def dollars(self):
        try:
            user_input = int(input("Enter £ "))
            print(f"= $", dollar * user_input)
        except:
            print("Numbers Only!")
            conversion.dollars()
        else:
            menu()

    def euros(self):
        try:
            user_input = int(input("Enter £- "))
            print(f"= €", euro * int(user_input))
        except:
            print("Numbers Only!")
            conversion.dollars()
        else:
            menu()

    def HKD(self):
        try:
            user_input = int(input("Enter £- "))
            print(f"= €", HKD * int(user_input))
            menu()
        except:
            print("Numbers Only!")
            conversion.dollars()
        else:
            menu()

    def TL(self):
        try:
            user_input = int(input("Enter £- "))
            print(f"= €", TL * int(user_input))
            menu()
        except:
            print("Numbers Only!")
            conversion.dollars()
        else:
            menu()


conversion = Conversion()


def menu():
    print("=======Welcome to Exchange=======")
    print("""=================================
--[0] Exit
--[1] Pounds to US Dollar
--[2] Pounds to Euros
--[3] Pounds to HKD 
--[4] Pounds to Turkish Lira""")
    while True:
        user_input = (input("-"))
        if (user_input) == "1":
            conversion.dollars()
        elif (user_input) == "2":
            conversion.euros()
        elif (user_input) == "3":
            conversion.HKD()
        elif (user_input) == "4":
            conversion.TL()
        elif (user_input) == "0":
            sys.exit()
        else:
            print("Choose from 0-4")
            continue


menu()
