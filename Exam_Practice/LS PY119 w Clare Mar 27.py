def count_duplicates(word):
    count = 0
    i = 1
    while i < len(word):
        if word[i - 1] == word[i]:
            count += 1
            i += 2
        else:
            i += 1
    
    return count

# Tests
print(count_duplicates('success'))  # 2
print(count_duplicates('aabbccc'))  # 3
print(count_duplicates('aabbcccc')) # 4

print("div_list")

def list_of_divisors(number):
    return [num for num in range(1, number + 1) if number % num == 0]

print(list_of_divisors(6)) #  [1, 2, 3, 6]
print(list_of_divisors(15)) # [1, 3, 5, 15]