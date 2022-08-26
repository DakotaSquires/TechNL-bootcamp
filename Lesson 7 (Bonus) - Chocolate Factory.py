# INPUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# employee number
while True:
    try:
        employee_number = int(input("Enter your employee number: "))
    except ValueError:
        print("Error. Make sure you enter only numbers.")
    else:
        break

# employee name
while True:
    try:
        employee_name = str(input("Enter your name: "))
    except ValueError:
        print("Error. Make sure you enter only letters.")
    else:
        break


location = str(input("Enter the location of your trip: "))

# vehicle used
while True:
    try:
        vehicle = str(input("Did you use your own ('own') car or did you rent ('rent') one? "))
    except ValueError:
        print("Error. Make sure you enter only letters.")
    else:
        break

# travel dates
while True:
    try:
        start_date = str(input("Enter the start date of your travel (format: MM/DD): "))
    except ValueError:
        print("Error. Make sure you enter only numbers with a slash between them.")
    else:
        break

# PROCESSING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
    try:
        end_date = str(input("Enter the return date of your travel (format: MM/DD): "))
    except ValueError:
        print("Error. Make sure you enter only numbers with a slash between them.")
    else:
        break

start_day = int(start_date[3:5])
end_day = int(end_date[3:5])
number_of_days = abs(end_day - start_day)

# OUTPUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if vehicle == "own":
    kms = int(input("Enter the total number of kilometers traveled: "))
    mileage = kms * 0.10
    if number_of_days <= 3:
        diem_short_own = 85 * number_of_days

        CA_diem_short_own = diem_short_own + mileage
        HST_diem_short_own = 0.13 * diem_short_own
        CT_diem_short_own = CA_diem_short_own + HST_diem_short_own
        print()
        print("Claim amount: " + str(CA_diem_short_own))
        print("HST amount: " + str(HST_diem_short_own))
        print("Claim total: " + str(CT_diem_short_own))

    elif number_of_days > 3:
        diem_long_own = 100 * number_of_days

        CA_diem_long_own = diem_long_own + mileage
        HST_diem_long_own = 0.13 + diem_long_own
        CT_diem_long_own = CA_diem_long_own + HST_diem_long_own
        print()
        print("Claim amount: " + str(CA_diem_long_own))
        print("HST amount: " + str(HST_diem_long_own))
        print("Claim total: " + str(CT_diem_long_own))


if vehicle == "rent":
    mileage_56 = 56 * number_of_days
    if number_of_days <= 3:
        diem_short_rent = 85 * number_of_days

        CA_diem_short_rent = diem_short_rent + mileage_56
        HST_diem_short_rent = 0.13 * diem_short_rent
        CT_diem_short_rent = CA_diem_short_rent + HST_diem_short_rent
        print()
        print("Claim amount: " + str(CA_diem_short_rent))
        print("HST amount: " + str(HST_diem_short_rent))
        print("Claim total: " + str(CT_diem_short_rent))

    elif number_of_days > 3:
        diem_long_rent = long_daily_rate = 100 * number_of_days

        CA_diem_long_rent = diem_long_rent + mileage_56
        HST_diem_long_rent = 0.13 * diem_long_rent
        CT_diem_long_rent = CA_diem_long_rent + HST_diem_long_rent
        print()
        print("Claim amount: " + str(CA_diem_long_rent))
        print("HST amount: " + str(HST_diem_long_rent))
        print("Claim total: " + str(CT_diem_long_rent))
