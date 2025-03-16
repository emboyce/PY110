numbers = [4, 5, 6, 7, 8]

for thing in range(len(numbers) - (len(numbers) - 1)):
    print("thing", thing)


nested = [numbers[:idx + 1]
          #for _ in range(len(numbers) - (len(numbers) - 1))
          for idx in range(len(numbers))]

nested = []
# for _ in range(len(numbers) - (len(numbers) - 1)):
for idx in range(len(numbers)):
    nested.append(numbers[:idx + 1])

print(nested) 