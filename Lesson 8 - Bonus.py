import sys

my_list = []

while True:
    user_input = int(input("Enter a number "))
    if user_input == 0:
        print()
        print("Entered list: ", my_list)
        my_list.sort()
        print()
        print("Sorted list: ", my_list)
        print()
        sys.exit("0 has been entered to stop the program")
    else:
        my_list.append(user_input)
        continue
