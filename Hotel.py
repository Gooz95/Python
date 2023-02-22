import sys

small_rooms_price = 20.0
large_room_price = 40.0



print()
print("===========================")
print("Welcome to Dawood's Hotel")
print("===========================")


# RETURN FUNCTION IF NAME IS NOT TYPED PROPER
def ask_name():
    while True:
        name = input("What is you're name? ")
        if name.isalpha():
            return name
        else:
            print("please enter a real name!")


print("Hello nice to meet you: " + ask_name())
print("==========================================")
print()
print("Small room price is £", small_rooms_price)
while True:
    try:
        small_rooms = int(input("how many small rooms would you like? "))
        break
    except ValueError:
        print("Please enter a number!...")
        print("=====================================")
        continue

print("Small room total £", float(small_rooms_price) * int(small_rooms), "Total")
print()
print("===========================================")
print()
print("Large room price is £", large_room_price)
while True:
    try:
        large_room = int(input("how many large rooms would you like? "))
        break
    except ValueError:
        print("Please enter a number!...")
        print("=====================================")
        continue

print("Thats £", float(large_room_price) * int(large_room), "Total")
print()
print("============================================")
print()
print("thats ", small_rooms, "small rooms", "and ", large_room, "large rooms")
Large_Total = float(large_room) * float(large_room_price)
Small_Total = float(small_rooms) * float(small_rooms_price)
Total = float(small_rooms) * float(small_rooms_price) + float(large_room) * float(large_room_price)
print()
print("==================Total==================")
print("Small room Total £", Small_Total)
print("Large room Total £", Large_Total)
print("Total £", Total)
print("==========================================")

while True:
    print("-Exit?")
    user_input = input("Y/N ")
    if user_input == "Y":
        sys.exit()
    else:
        ask_name()
