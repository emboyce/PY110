print("q16")

'''
7:34 7 min
P:
- in: str
- out: count of distinct case-insensitive alpha characters and numeric
digits that appear more than once in the string
E:
- input is only alphanumeric
- case insensitive
- count anything that appears more than once
D:
- dictionary to hold characters and counts
- input string
- output count
A:
- create a dictionary of characters and character counts
    - for each char in the string:
        add lower char to the dict with default value 1, or increment
- check value of each item in the dict
    - increment count if value is greater than 1
- return count
'''

def distinct_multiples(str):
    str = str.lower()
    char_counts = {}
    for char in str:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    count = 0
    for value in char_counts.values():
        if value > 1:
            count += 1
    
    return count

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

print("q17")

'''
7:42 15 min and it was a hard question
P:
in: list of ints
out: min int that can be appended to list, so list sums to next prime
    that is greater than sum of numbers
E:
- list will have 2+ ints
- all values positive
- may be multiples in list
D:
- helper function - next prime number
- input list
- sum of list
- output integer
A:
- helper function - next prime
    - take a number, output the next prime number
    - prime if the number divided by all ints lower than sqrt num
        do not divide evenly
    - increment number
        - check if prime
    - if not increment number until prime
- helper function - is prime
    - find sqrt number === num ** (1/2), round up for safety
    - for all numbers less (except 1), return false if num % num == 0

- sum input list
- find next prime up, return increment to prime
- return increment
'''

def is_prime(num):
    sqrt = int(num ** (1/2))
    for i in range(2, sqrt + 1):
        if num % i == 0:
            return False
    
    return True

def next_prime_incr(num):
    incr = 1
    while True:
        if is_prime(num + incr):
            return incr
        
        incr += 1

def nearest_prime_sum(numbers):
    num_sum = sum(numbers)
    return next_prime_incr(num_sum)


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

print("q18")

'''
8:21 13 min
P:
in: list of ints (may be negative)
out: index n for which all numbers with index less than N sum to
    same value as numbers with index greater than N
E:
- never count the number at the index
- if no valid number, return -1
- if multiple answers, return result with lowest value
- the nothingness to the left of the list sums to zero
D:
- input list
- output index int
- 2 sub-lists to sum by slicing
A:
- start at index zero
- compare the slice from [- 1:index] and [index + 1 : ]
- if they sum equally, return index
    - I think actually it's index
- otherwise return -1
'''

def equal_sum_index(nums):

    for idx in range(0, len(nums) - 1):
        sum_left = sum(nums[0 : idx])
        sum_right = sum(nums[idx + 1 : ])
        if sum_left == sum_right:
            return idx
        
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

print("q19")

'''
8:34 13 min w troubleshooting
P:
- in: list of ints, may be neg or zero
- out: the int that appears an odd number of times
E:
- there will always be exactly one such integer
- list is not empty
D:
- input list
- output integer
- dictionary of integers and values
    - be mindful of str/int
A:
- create a dictionary
    - keys are strings of integers
    - values are counts of integers in list
        - fine to rewrite keys with counts, always the same anyway
- for items in list, if value is odd return key

'''

def odd_fellow(ints):
    dict_counts = {str(digit):ints.count(digit) for digit in ints}

    for key, value in dict_counts.items():
        if value % 2 == 1:
            return int(key)
        
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

print("q20")

'''
P:
8:47 7 min but it kinda sucks
- in: list of numbers, all the same except one
- out: number in list that differs
E:
- list always min 3 numbers
- always exactly one number that's different
D:
- dict of numbers and counts
- input list
- output int
A:
- create a dict of str(nums) keys and count values
- iterate through items in the dictionary and return the one that
has a count greater than 1
- return the INT of the key
'''

def what_is_different(nums):
    dict_nums = {str(digit): nums.count(digit) for digit in nums}

    for key, value in dict_nums.items():
        if value == 1:
            if "." in key:
                return float(key)
            else:
                return int(key)
    return None

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

print("q20-alternate")

'''
8:55

- throw it into a set
- for each item in the set
    - check if list[0] is the thing
        - if yes, pop it out of the list
        - if it's still in the list, return the other thing
        - if not, return the item
    if it's not the thing, check the next thing at [1]
'''

def what_is_different(nums):
    set_nums = set(nums)
    for item in set_nums:
        if nums[0] == item:
            nums.pop(0)
            if item in nums:
                continue
            else:
                return item
        elif nums[1] == item:
            continue
        else:
            return item
        
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

print("q15 again")

'''
3:32 10 min
P:
- in - str of numeric digits
- out - greatest product of 4 consecutive digits
E:
- argument will always have more than 4 digits
- return as integer not string
- product of consecutive digits
D:
- max_product and product
- index for start position
- input string
- output integer
- intermediate list of integers
A:
- convert the string to a list of integers
- set max product to zero
- starting at index zero, compute the product
    - lowest index 0, greatest index len(string) - 4
        - 23456
        0 = 2
        1 = 3
        len(str) = 5
        5 - 4 = 1 > need range 2, so range is (len(str) - 3)
- compare to max product
    - if greater, replace max product
- return max product
'''

def greatest_product(digits):
    ints = [int(digit) for digit in digits]
    max_product = 0

    for idx in range(len(digits) - 3):
        product = ints[idx]*ints[idx+1]*ints[idx+2]*ints[idx+3]
        if product > max_product:
            max_product = product
    
    return max_product
    

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6