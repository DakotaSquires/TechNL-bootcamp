# Lesson 6 -problem a - Birthday Email

name = input("Please enter recipient name ")
birthday = input("Please enter recipient birth date ")
birth_year = int(input("Please enter the year the recipient was born "))
sender = input("Please enter sender name ")

year = 2022


def birthday_age():
    age = year - birth_year
    return age


print(" ")
print("Greetings", name, ",")
print(" ")
print("I heard that", birthday, ", is your birthday and that you are turning", birthday_age(), "today. I just wanted to wish you all the best on this special day!")
print(" ")
print("Warmest wishes,")
print(" ")
print(sender)
