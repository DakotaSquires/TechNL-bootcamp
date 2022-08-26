# INPUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# PROCESSING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# addition
sum_one = sum(matrix[0])
sum_two = sum(matrix[1])
sum_three = sum(matrix[2])
sum_total = sum_one + sum_two + sum_three

# length
length_one = len(matrix[0])
length_two = len(matrix[1])
length_three = len(matrix[2])
length_total = length_one + length_two + length_three


# OUTPUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Each list has a sum as follows, for a total of", sum_total)
print("List one:", sum_one)
print("List two:", sum_two)
print("List three:", sum_three)
print()
print("The over all list has length:", len(matrix))
print()
print("Each list has a length as follows, for a total of", length_total)
print("List one:", length_one)
print("List two:", length_two)
print("List three:", length_three)
