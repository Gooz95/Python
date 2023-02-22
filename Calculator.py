# add function
def add(input1, input2):
    return input1 + input2


# subtract
def subtract(input1, input2):
    return input1 - input2


# multiply
def multiply(input1, input2):
    return input1 * input2


# divide
def divide(input1, input2):
    return input1 / input2


# Main menu

print("Select Function")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input("Select Option: ")

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid try again.")
            continue

        if choice == "1":
            print(num1, "+", num2, "=", add(num1,num2))

        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1,num2))

        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1,num2))

        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1,num2))

        while True:
            retrycalculation = input("Want to choose another option? (yes/no): ")
            if retrycalculation == "no":
                exit()
            elif retrycalculation == "yes":
                break
            else:
                print("Invalid Input")
                continue






