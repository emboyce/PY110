print("q6")

'''
9:47 10 min or less
P:
- in: string
- out: dict, keys are lowecase letters, values are letter frequency
Rules:
- ignore anything that's not a lowercase letter
- empty string or string with no lowercase letters returns empty dict
D:
- input string
- output dict
A:
- create empty dict
- index through the string by char
- if the char is alpha and is lowercase, then:
    - if the char is already in the dict, increment the value by 1
    otherwise:
        - add the char to a dictionary
        - set the value to 1
- return the dict

'''

def count_letters(str):
    output = {}
    for char in str:
        if char in output:
            output[char] += 1
        elif char.islower() and char.isalpha():
            output[char] = 1
    return output

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

print("q7")

'''
P:
in: list of ints
out: number of identical pairs in the list
E:
rules:
- if list is empty or 1 value, return 0
- count full pairs, ie 5 instances is 2
D:
- input list
- output integer
- count variable
A:
- set count to zero
- sort input list
- starting at the first element, if it's the same as the next element
    pop them both out of the list and increment the count
- otherwise just pop the first element and don't increment count
- continue until list length is < 2
- return the count

11 min or so
'''

def pairs(nums):
    numbers = sorted(nums)
    count = 0

    while len(numbers) >= 2:
        if numbers[0] == numbers[1]:
            numbers = numbers[2:]
            count += 1
        else:
            numbers = numbers[1:]

    return count

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

print("q8")

'''
10:11 10:28 17 min

P:
in: non-empty string of only lowercase alphas
out: length of longest vowel substring
E:
rules:
- aeiou
- order doesn't matter
D:
- input string
- output integer
- length counter
- max length counter
- vowels const
- index, test index
A:
- start at index 0, test index 0
- while test index < len of string
    - check if char at test index is in vowels
    - if yes, increment test counter
    - if no
        - check if test counter > max counter 
        - if yes set max to test
        - set test to 0
        - set index to ...actually I don't think we even need the index
- return max counter

'''

def longest_vowel_substring(str):
    VOWELS = "aeiou"
    idx = 0
    max_vowels = 0
    counter = 0

    while idx < len(str):
        if str[idx] in VOWELS:
            counter += 1
            idx += 1
            if idx == len(str):
                if counter > max_vowels:
                    max_vowels = counter
        else:
            if counter > max_vowels:
                max_vowels = counter
            counter = 0
            idx += 1
    
    return max_vowels

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

print("q9")

'''
> FEEDBACK: Can you use .count?
10:28 3 min
10:31 11 min
P:
in: 2 strings
out: number of times second string occurs in the first string
E:
rules:
- no overlaps
- second arg is never an empty string
- first str may be empty
D:
- input strings
- output int
- bunch of slice sub-lists
A:
- search for the start index of the string in ever-smaller slices

- set counter to zero
- while len of string is >= len of substring
    - with full string, find start index of sub-string
    - if -1, break out of loop
    - if found:
        increment counter
        set string to string slice from [find(substring) + len(substring):]
- return counter

'''

def count_substrings(str1, str2):
    #return str1.count(str2)
    count = 0
    while len(str1) >= len(str2):
        if str1.find(str2) == -1:
            break

        count += 1
        str1 = str1[str1.find(str2) + len(str2) : ]
    
    return count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

print("q10")

'''
11:11 LONG - 45 min?
TAKEAWAY: range + [:end] together is minus two from len
P:
- in: string of digits
- out: number of even-numbered substrings of all lengths
E:
- count repeating substrings as duplicates
D:
- helper function - list of substrings
    - list of number substrings
- input string of digits
- output integer
A:
- helper: generate all substrings
 - for index in string, substring from index + 1 to length of string
- for str in list, if int(str) % 2 == 2 then increment counter
- return counter

'''

def substrings(str1):
    subs = [str1[i:j] for i in range(len(str1))
                      for j in range(i + 1, len(str1) + 1)]
    print(subs)
    return subs
        
def even_substrings(str):
    count = 0
    subs = substrings(str)

    for s in subs:
        if int(s) % 2 == 0:
            count += 1
    
    return count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

print("q11")

'''
5:02 11 min
add chars to the string until it's equal to the next equal number
of characters as the original string and multiplies to the total
P:
in: s
out: tuple (t (string), k (count of string))
E:
- use shortest possible substring
D:
- input string
- output tuple (string, count)
A:
- test increasingly long sub-strings:
    - substring length <= string length
    - len(string) % len(substring) == 0
    - substring * above = string
'''

def repeated_substring(s):
    idx = 1

    while idx <= len(s):
        t = s[0:idx]
        if len(s) % len(t) == 0:
            k = len(s) // len(t)
            if  k * t == s:
                return (t, k)
        idx += 1

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

print("q12")

'''
5:13 7 min
P:
- in: sentence
- out: True/False
E:
- case is irrelevant
- must contain every letter of the alphabet at least once
D:
- input string
- output boolean
- set for comparison by sort
A:
- create a set of all distinct letters in the string
- count length - should be 26
'''

import string
ALPHA = string.ascii_lowercase

def is_pangram(phrase):
    phrase_set = {char.lower() for char in phrase
                                if char.isalpha()}
    return len(phrase_set) == 26

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

print("q13")

'''
> FEEDBACK: This is a lot easier to do if repeats are allowed
5:22 < 15 min
P:
in: string1, string2
out: True/False
E:
rules:
- strings contain only lowercase alphas
- no empty strings
- return true of some portion of chars in str1 can be arranged into str2
D:
- str1, str2 inputs
- True/False output
- list of first string, so we can pop items out
A:
- iterate through the second string
    - for each character, if the character is not in str1 return False
    - if it is, pop the character out of str1 and continue
'''

def unscramble(str1, str2):
    letters = list(str1)
    for char in str2:
        if not char in letters:
            return False
        
        letters.pop(letters.index(char))
    
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)

print("q14")

'''
5:38 6 min
P:
- in: integer number, pos or neg or zero
- out: sum of multiples of 7 or 11, less than number
E:
rules:
- if multiple of both 7 and 11, only count once
- if zero, return zero
- if negative, return zero
D:
- list of multiples
- input int
- output sum int
A:
- if zero or negative, return 0
- run through numbers up to the number (< num)
- if the number is a multiple of 7 or 11, add it to a list
- sum the list and return
'''
def seven_eleven(target):
    if target <= 0:
        return 0
    
    multiples = [num for num in range(1, target)
                     if num % 7 == 0 or num % 11 == 0]
    
    return sum(multiples)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

print("q15")

'''
5:45 15 min SCRAPPY AS SHIT
P:
in: string of digits
out: greatest product of 4 consecutive digits, as int
E:
- string will always have more than 4 digits
- no negatives or weirdness
D:
- input string
- list of individual numeric digits
- list of final 4 digits
- product of final 4 digits
A:
- convert the string to a list of ints
- find all sequential 4 digit sets
    - start at index 0 : index 3 (slice 4, idx + 4, range 5)
    - stop at index (length of list - 4)
        23456
        0:4, 1:5
- multiple all sequential 4 digit sets
    - the highest sum will have the highest product
    - sum and find index of max
    - use same index on seqs
    - multiply out this seq index
- return maximum sum
'''

def greatest_product(digits):
    ints = [int(digit) for digit in digits]
    seqs = [ints[idx : idx + 4] for idx in range(len(ints) - 3)]

    import math
     
    products = [math.prod(item) for item in seqs]

    return max(products)

    '''sums = [sum(seq) for seq in seqs]
    idx_sum = max(sums)
    idx = sums.index(idx_sum)
    consec = seqs[idx]
    
    return consec[0]*consec[1]*consec[2]*consec[3]'''

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6