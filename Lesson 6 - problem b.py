# lesson 6 - problem b - "Sum up"

user_input = int(input("Enter a number "))


def sum_up_to(x):
    total = 0
    i = 0
    while i <= x:
        total = total + i
        i += 1
    return total


print(sum_up_to(user_input))
