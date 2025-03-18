error = ("There is no possible number that fulfills" 
             "those requirements.")

def next_featured(num):
    MAX = 9876543201
    diff_7 = num % 7
    next_7 = num + (7 - diff_7)
    if next_7 % 2 == 0:
        next_7 += 7

    for feature in range(next_7, MAX + 1, 14):
        if len(set(str(feature))) == len(str(feature)):
            return feature
    
    return error



print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

print(next_featured(9876543201) == error)       # True