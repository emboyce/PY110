from pprint import pprint

print("q1")

def invert_dict(dictionary):
    return {value:key for key, value in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

print("q2")

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}

def keep_keys(dictionary, key_list):
    return {key:value for key, value in dictionary.items() 
                      if key in key_list}
print(keep_keys(input_dict, keys) == expected_dict) # True

print("q3")

# All of these examples should print True
VOWELS = "aeiou"

def remove_vowels0(str_list):
    word_list = []
    for word in str_list:
        no_vowel_word = ""
        for char in word:
            if char.lower() not in VOWELS:
                no_vowel_word += char
        word_list.append(no_vowel_word)
    return word_list

def no_vo_word(word):
    no_vo = "".join([char for char in word if char.lower() not in VOWELS])
    return no_vo

def remove_vowels(str_list):
    return [no_vo_word(word) for word in str_list]


original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

print("q4")

def word_lengths0(word_str=""):
    word_list = word_str.split()
    return [word + " " + str(len(word)) for word in word_list]

def word_lengths(string=''):
    return [f"{word} {len(word)}"
            for word in string.split()]


# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True

print("q5")

def multiply_items(lst1, lst2):
    return [lst1[idx] * lst2[idx] for idx in range(len(lst1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

print("q6")

def sum_of_sums0(nums):
    return sum([num for idx in range(len(nums))
                    for num in nums[0:idx+1]])

def sum_of_sums(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]*(len(nums) - i)
    return total

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True

print("q7")

def sum_digits(num):
    return sum([int(digit) for digit in str(num)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

print("q8")

def staggered_case(string):
    return "".join([char.upper() 
                    if idx % 2 == 0 and char.isalpha()
                    else char.lower()
                        for idx, char in enumerate(string)])

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string))

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")  

print("q9")

def staggered_case2(string):
    switch = True
    new_string = ""
    for char in string:
        if switch == True:
            new_string += char.upper()
            if char.isalpha():
                switch = False
        else:
            new_string += char.lower()
            if char.isalpha():
                switch = True
    return new_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case2(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case2(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case2(string) == result)  # True

print(staggered_case2('') == "")          # True

print("q10")

def unique_sequence0(nums):
    if not nums:
        return []
    result = [nums[0]]
    resulter = [result.append(num) for num in nums if result[-1] != num]
    return result

def unique_sequence(nums):
    return [num for idx, num in enumerate(nums)
                if idx == 0 or nums[(idx - 1)] != num]

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

print(unique_sequence([]))