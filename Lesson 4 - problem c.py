#input

user_input = int(input("Please enter your age "))

#processing

movies = str("Movies available for you:")
g = str("G rated")
pg = str("PG rated")
all = str("all movies, unrestricted")

child = str("$1.00")
teen = str("$5.00")
adult = str("$10.00")
senior = str("$3.50")

#output

if user_input < 13:
    print(str(movies), str(g))
    print(str("Admission costs:"), child)
if 13 <= user_input <= 17:
    print(str(movies), str(g), str(","), str(pg))
    print(str("Admission costs:"), teen)
if 18 <= user_input <= 59:
    print(str(movies), str(all))
    print(str("Admission costs:"), adult)
if user_input >= 60:
    print(str(movies), str(all))
    print(str("Admission costs:"), senior)
