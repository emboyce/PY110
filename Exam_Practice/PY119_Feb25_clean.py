# Can you generate this output using a nested list comprehension?
# [ [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5] ]

numbers = [13, 27, 3, 45, 500]

nested = [[idx + 1 for idx in range(i)]
                   for i in range(1, len(numbers) + 1)]

better_nested = [[numbers[idx] for idx in range(i)]
                               for i in range(1, len(numbers) + 1)]

print(nested)
print(better_nested)
