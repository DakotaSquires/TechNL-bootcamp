# Lesson 4 - Problem d) - Buying Pillows

# input

user_input1 = int(input("Number of pillows: "))
user_input2 = str(input("Priority shipping: "))

# processing

tax = 1.15

reg_pill_cost = 21 * user_input1
bulk_pill_cost = 15.58 * user_input1

pri_ship_cost = user_input1 * 2 + 60
reg_ship_cost = user_input1 * 1.25

subtotal_of_reg_pill_pri_ship = reg_pill_cost + pri_ship_cost
subtotal_of_reg_pill_reg_ship = reg_pill_cost + reg_ship_cost
subtotal_of_bulk_pill_reg_ship = bulk_pill_cost + reg_ship_cost
subtotal_of_bulk_pill_pri_ship = bulk_pill_cost + pri_ship_cost

# output

if user_input1 < 10 and user_input2 == "yes":
    print(str("Unit cost:"))
    print(reg_pill_cost)
    print(str("Shipping cost:"))
    print(pri_ship_cost)
    print(str("Subtotal:"))
    print(round(subtotal_of_reg_pill_pri_ship, 2))
    print(str("Tax"))
    print(round(0.15 * subtotal_of_reg_pill_pri_ship, 2))
    print(str("Total:"))
    print(round(tax * subtotal_of_reg_pill_pri_ship, 2))
    print(" ")
    print("Thank you for your order!")

elif user_input1 < 10 and user_input2 == "no":
    print(str("Unit cost:"))
    print(reg_pill_cost)
    print(str("Shipping cost:"))
    print(reg_ship_cost)
    print(str("Subtotal:"))
    print(round(subtotal_of_reg_pill_reg_ship, 2))
    print(str("Tax"))
    print(round(0.15 * subtotal_of_reg_pill_reg_ship, 2))
    print(str("Total:"))
    print(round(tax * subtotal_of_reg_pill_reg_ship, 2))
    print(" ")
    print("Thank you for your order!")

elif user_input1 >= 10 and user_input2 == "no":
    print(str("Unit cost:"))
    print(bulk_pill_cost)
    print(str("Shipping cost:"))
    print(reg_ship_cost)
    print(str("Subtotal:"))
    print(round(subtotal_of_bulk_pill_reg_ship, 2))
    print(str("Tax"))
    print(round(0.15 * subtotal_of_bulk_pill_reg_ship, 2))
    print(str("Total:"))
    print(round(tax * subtotal_of_bulk_pill_reg_ship, 2))
    print(" ")
    print("Thank you for your order!")

elif user_input1 >= 10 and user_input2 == "yes":
    print(str("Unit cost:"))
    print(bulk_pill_cost)
    print(str("Shipping cost:"))
    print(pri_ship_cost)
    print(str("Subtotal:"))
    print(round(subtotal_of_bulk_pill_pri_ship, 2))
    print(str("Tax"))
    print(round(0.15 * subtotal_of_bulk_pill_pri_ship, 2))
    print(str("Total:"))
    print(round(tax * subtotal_of_bulk_pill_pri_ship, 2))
    print(" ")
    print("Thank you for your order!")

else:
    print(" ")
    print("Error. Please try again.")