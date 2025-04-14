print("q1")

'''
input: list of nums
output: list of nums, each is how many nums are smaller
rules:
- only count unique values
- no boundaries
data:
input list
intermediary set for unique comparison
output list
algorithm:
use a list comprehension with a set and helper function
helper: return count of unique nums smaller than num in a list
- make a set of the list
- for each item in the set, increment counter if it's smaller than num
- return counter

- for each num in list, run helper function and add result to a new list
- return the new list
12 min
'''

def uniques(num, lst):
    counter = 0
    for item in set(lst):
        if item < num:
            counter += 1
    return counter

def smaller_numbers_than_current(nums):
    output = [uniques(num, nums) for num in nums]
    return output


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

print("q2")

'''
In: list of ints, may be negative
out: min sum of 5 consecutive ints
rules:
- if length of list less than 5, return None
- no boundaries
data:
- input list of ints
- all possible sub-lists of 5 consecutive integers
    array of arrays
algorithm:
find all sub-lists. Use min function to find minimum for each and store it.
Find the lowest min and return that.

helper: sub-lists - return all 5-length sub-lists of a list
- 2 indices
- start with lower index at len(list) - 5
- use list slicing with indices
- store to array of arrays
- bump both indices down until the lower one is zero
- return array

- check if len list < 5 - if yes return None
- create array of sublists with helper
- use comprehension to create array of minimum sums
    - sum(arr) for each array in sub-list
- return minimum of minimums

13 min

'''

def sub_arrays(lst):
    high_idx = len(lst)
    low_idx = len(lst) - 5
    output = []
    
    while low_idx >= 0:
        output.append(lst[low_idx : high_idx])
        low_idx -= 1
        high_idx -= 1
    
    return output

def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    subs_lst = sub_arrays(lst)

    mins_lst = [sum(arr) for arr in subs_lst]

    return min(mins_lst)

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

print("q3")

'''26
in: string
out: copy of string, every 2nd char in every 3rd word converted to uppercase
rules:
words separated by spaces
no weirdness
data:
input string
output string
list of words
algorithm:
have to convert to a list to index by word. Then can index in string. Then
join back into list.
- convert string to list by splitting
- iterate through list items and indices. If index + 1 / 3 == 0, 
    change word
- helper: change word
    - take word, replace 2nd char with upper for every 2nd char
        - iterate through char, idx in word
            - if idx % 2 == 1, change char to upper
            - add char to string
    - return word
- rejoin list into string
- return string

11 min
'''

def word_change(word):
    new_word = ""
    for idx, char in enumerate(word):
        if idx % 2 == 1:
            new_word += char.upper()
        else:
            new_word += char
    return new_word

def to_weird_case(phrase):
    phrase_lst = phrase.split()
    word_lst = [(word_change(word) if (idx + 1) % 3 == 0 else word) 
                                   for idx, word in enumerate(phrase_lst)]
    return " ".join(word_lst)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

print("q4")

'''
input: list of integers
output: tuple of closest integers

rules:
- all positive ints
- if multiple equally close, return first pair

data:
- input list
    - sorted input list
- list of lists containing difference, 2 items
    - sorted list of this
- output tuple

algorithm:
- sort the input list
- run through the list, stopping 1 before the last item
- at each stop, create a sub-list of difference, item at index, next item
- sort the list of sub-lists
- convert the last 2 elements of the first item to a tuple
- return the tuple
'''

def closest_numbers0(nums):
    sorts = sorted(nums)
    sub_lists = [[(sorts[idx + 1] - sorts[idx]), sorts[idx], sorts[idx + 1]] 
                 for idx in range(len(sorts) - 1)]
    ordered_subs = sorted(sub_lists)

    first_index = nums.index(ordered_subs[0][1])
    second_index = nums.index(ordered_subs[0][2])

    if first_index > second_index:
        first_index, second_index = second_index, first_index

    return tuple([nums[first_index], nums[second_index]])

'''
run through each item in the list, and compare it to each other item
find the difference (abs)
store the minimum difference, and the indices for that difference
create a tuple at those indices
return the tuple

8:06, 30 min

FEEDBACK: can the tuple be in the other order?
'''

def closest_numbers(nums):
    min_diff = max(nums) - min(nums)
    idx1 = None
    idx2 = None

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            diff = abs(nums[i] - nums[j])
            if diff < min_diff:
                idx1 = i
                idx2 = j
                min_diff = diff
    
    return (nums[idx1], nums[idx2])


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

print("q5")

'''
8:08 8:24 16 min even with having to do it over

TAKEAWAY: if order has to be preserved, don't sort the damn thing
ALSO if you can avoid doing all steps for all values, may not be
    best to do a comprehension
ALSO questions may be geared for those who struggle with comprehensions
    (and coding)

in: string
out: char that occurs most often in the string

rules:
- if tie, return earliest char in string
- case insensitive

data:
- input string and lowercase version
- list of tuples of char, count of char
- sorted list
- output char

algorithm:
- convert string to lowercase
- set the max count to zero
- interate over the chars in the string
- for each char, if the count is higher than the max
    - store the char
    - set the new max
- output the char

'''

def most_common_char(phrase):
    phrase = phrase.casefold()
    max_count = 0
    max_char = None

    for char in phrase:
        if phrase.count(char) > max_count:
            max_char = char
            max_count = phrase.count(char)
    
    return max_char

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
