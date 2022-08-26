#Lesson 4 - Problem a) - Long Distance Calling

#inputs

user_input1 = input("Calling location ")
user_input2 = input("Call destination ")
user_input3 = float(input("Duration of call "))

#processing

start_rate = float(1.3)
additional_charge = float(user_input3) - 1
exact_cost = float(start_rate + additional_charge * 0.05)
total_cost = round(exact_cost, 2)

#output

if user_input3 <= 0:
    print(" ")
    print("Error. The number entered is less than or equal to zero. Please try again.")
else:
    print(" ")
    print("Call:", str(user_input1), "to", str(user_input2))
    print("Duration:", float(user_input3))
    print("Total call cost: $", float(total_cost))
    print("Thank you")
