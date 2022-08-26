# INPUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Customers = {
    "Daniel": "555-5555",
    "Anna": "555-7777",
    "Linus": "555-6666",
}

Customers["Bob"] = '555-2222'

# OUTPUTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# part a
print("All contacts:")
for key in Customers:
    value = Customers[key]
    print(f"{key} = {value}")

# extra
print()
print('All contact names:')
print(Customers.keys())

# part b
print()
print("All phone numbers in Contacts:")
print(Customers.values())

# part c
print()
print("Number of contacts: ", len(Customers))

# part d
print()
print("----------")
print()
if "Daniel" in Customers:
    print("Daniel's number: ", Customers.get("Daniel"))
