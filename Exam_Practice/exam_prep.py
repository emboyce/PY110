d1 = {"a": 1, "b": 2,}
x = all(d1)

print(x)

def slower(str):
    return str[-1]
    

animals = ['Cat', 'dog', 'ZEBRA', 'monkey']
sorted_animals = sorted(animals, key=slower)
print(sorted_animals)
# Expected output: ['Cat', 'dog', 'monkey', 'ZEBRA']
# Actual output:   ['Cat', 'ZEBRA', 'dog', 'monkey']