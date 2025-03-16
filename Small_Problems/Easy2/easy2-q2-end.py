print("q2")

def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 | set2

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

print("q3")

def halvsies(nums):

    if len(nums) % 2 == 0:
        split_index = len(nums) // 2
    else:
        split_index = (len(nums) // 2) + 1

    return [nums[:split_index], nums[split_index:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

print("q4")

def find_dup(nums):
    numbers = nums.copy()
    while True:
        value = numbers.pop()
        if value in numbers:
            return value

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True


print("q5")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]

def interleave0(lst1, lst2):
    output = []
    for idx in range(len(lst1)):
        output.extend([lst1[idx], lst2[idx]])
    return output

def interleave(lst1, lst2):
    output = []
    tup_list = list(zip(lst1, lst2))
    for tup in tup_list:
        output.extend(tup)
    print(output)
    return output

print(interleave(list1, list2) == expected)      # True

print("q6")

def multiplicative_average(nums):
    mults = 1
    for num in nums:
        mults *= num
    result = mults/len(nums)
    return f"{result:.3f}"
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

print("q7")

list1 = [3, 5, 7]
list2 = [9, 10, 11]

def multiply_list(lst1, lst2):
    lst3 = zip(lst1, lst2)
    return [elem[0]*elem[1] for elem in lst3]

print(multiply_list(list1, list2))
print(multiply_list(list1, list2) == [27, 50, 77])  # True

print("q8")
def digit_list(num):
    return [int(char) for char in str(num)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

print("q9")

vehicles = ['car', 'car', 'TRUCK', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

def count_occurrences(motos):
    moto_set = set([moto.casefold() for moto in motos])
    for item in moto_set:
        print(f"{item} => {motos.count(item)}")

count_occurrences(vehicles)

print("q10")

def average(nums):
    return sum(nums) // len(nums)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True