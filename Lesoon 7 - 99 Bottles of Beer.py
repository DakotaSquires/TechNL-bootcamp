# input

while True:
    try:
        bottle_number = int(input("How many bottles are on your wall? "))
    except ValueError:
        print("Error. Please enter a whole number.")
    else:
        break


# output
while True:
    print(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer")
    print("Take one down, pass it around")
    bottle_number -= 1
    print(f"{bottle_number} bottles of beer on the wall")
    print()
    if bottle_number == 2:
        print("1 bottle of beer on the wall, 1 bottle of beer")
        print("Take it down, pass it around")
        print("No more bottles of beer on the wall")
        break
    else:
        continue

