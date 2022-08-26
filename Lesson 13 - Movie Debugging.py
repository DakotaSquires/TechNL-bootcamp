# Movie therater Debugging

name = input("Please enter your name ")
age = int(input("Please enter your age "))

if age < 13:
    print("Hello " + name + ", you are allowed to view G rated movies. "
                            "The cost of admission is $5.00")
elif 13 <= age <= 17:
    print("Hello " + name + ", you are allowed to view PG-13 or G rated movies. "
                            "The cost of admission is $15.00")
elif 18 <= age <= 59:
    print("Hello " + name + ", you are allowed to view any movie unrestricted. "
                            "The cost of admission is $10.00")
elif age >= 60:
    print("Hello " + name + ", you are allowed to view any movie unrestricted. "
                            "The cost of admission is $3.50 with your senior's discount!")