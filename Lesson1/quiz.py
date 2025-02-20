dict1 = {"x":"y"}

dic2 = ()

listy = [1,2]
listy += [None]
print(listy)
lusty = []
print(len(lusty))

def less_than(upper_limit):
    numbers = []
    candidate = 1

    while True:
        numbers.append(candidate)
        candidate += 1
        if candidate > upper_limit:
            break

    return numbers

print(less_than(5))

1, 2, 3, 4,  
2, 3, 4, 5, 