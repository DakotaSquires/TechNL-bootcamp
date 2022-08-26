import sys

# input ------------------------------------------------------

user_input = int(input("How many pizza would you like to order? "))
user_region = str(input("What country are you ordering from? "))

if user_input <= 0:
    sys.exit("Error. Please try again.")

# processing ------------------------------------------------------

regular_price = user_input * 10

first_fifty = 50 * 10 - 10
after_fifty = user_input - 50
discount_fifty = first_fifty + after_fifty * 5

# output ------------------------------------------------------

# CANADA
if user_region == "canada" or user_input >= 500:
    print("Your total is: $", user_input * 3.75)
# USA
elif user_region == "us" and 1 <= user_input <= 10:
    print("Your total is: $", user_input * 7.50)
elif user_region == "us" and 11 <= user_input <= 19:
    print("Your total is: $", regular_price - 10)
elif user_region == "us" and 20 <= user_input <= 29:
    print("Your total is: $", regular_price - 20)
elif user_region == "us" and 30 <= user_input <= 39:
    print("Your total is: $", regular_price - 30)
elif user_region == "us" and 40 <= user_input <= 49:
    print("Your total is: $", regular_price - 40)
elif user_region == "us" and 50 <= user_input <= 59:
    print("Your total is: $", discount_fifty - 50)
elif user_region == "us" and 60 <= user_input <= 69:
    print("Your total is: $", discount_fifty - 60)
elif user_region == "us" and 70 <= user_input <= 79:
    print("Your total is: $", discount_fifty - 60)
elif user_region == "us" and 80 <= user_input <= 89:
    print("Your total is: $", discount_fifty - 80)
elif user_region == "us" and 90 <= user_input <= 99:
    print("Your total is: $", discount_fifty - 90)
else:
    print("ERROR")