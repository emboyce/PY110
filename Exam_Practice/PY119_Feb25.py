# Can you generate this output using a nested list comprehension?
# [ [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5] ]

numbers = [1, 2, 3, 4, 5]

for_take_1 = []
for i in range(1, len(numbers) + 1):
    inner = []
    for j in range(1, i + 1):
        inner.append(j)
    for_take_1.append(inner)

for_take_2 = []
for i in range(1, len(numbers) + 1):
    for_take_2.append(list(range(1, i + 1)))

not_nested_1 = [list(range(1, i + 1)) for i in range(1, len(numbers) + 1)]

def generate_list(num):
    return [num for num in range(1, num + 1)]

not_nested_2 = [generate_list(num) for num in range(1, len(numbers) + 1)]

nested = [[idx + 1 for idx in range(i)]
                   for i in range(1, len(numbers) + 1)]


for_take_3 = []
for i in range(1, len(numbers) + 1):
    inner = [j for j in range(1, i + 1)]
    for_take_3.append(inner)


print(for_take_1)
print(not_nested_1)
print(for_take_2)
print(not_nested_2)
print(nested)

sub_nested = [idx + 1 for idx in range(i)]
print(sub_nested)

print(for_take_3)

'''

'''