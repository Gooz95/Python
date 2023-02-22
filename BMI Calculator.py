

print("============================================================")
while True:
    try:
        Kg = float(input("Enter you Weight in KG: "))
        break
    except ValueError:
        print("Please enter a number!...")
        print("=====================================")
        continue
# Loop if not input correctly returns you to input again
print("============================================================")
while True:
    try:
        height_Metres = float(input("Enter your Height in CM: "))
        break
    except ValueError:
        print("Please enter a number!...")
        print("=====================================")
        continue
print("============================================================")
Bmi = float(Kg) / float(height_Metres / 100) ** 2
print()
print("==========================RESULTS===========================")
print(f"You'r BMI is: {Bmi}")
if Bmi <= 18.4:
    print("You are 'Underweight please eat'.")
elif Bmi <= 24.9:
    print("You are 'Normal Weight'"
          " \nCongratulations keep it up!'")
elif Bmi <= 29.9:
    print("You are 'Over Weight please get active'")
elif Bmi <= 34.9:
    print("Obesity 'Class 1'")
elif Bmi <= 39.9:
    print("Obesity 'Class 2'")
elif Bmi >= 40.0:
    print("Obesity 'Class 3 please seek help!'")
print("==========================================================")
print()
print("----------BMI TABLE---------------")
print("18.4 or Less   Under Weight------|")
print("18.5 to 24.9   Normal Weight-----|")
print("25 to 29.9     Over Weight-------|")
print("30 to 34.9     Obesity (Class 1)-|")
print("35 to 39.9     Obesity (Class 2)-|")
print("40 to Above    Obesity (Class 3)-|")
print("==================================")










