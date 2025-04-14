"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Constraints:

0 <= len(digits) <= 4
digits[i] is a digit in the range ['2', '9'].

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

MAP = {'2': "abc ", '3': 'def ', '4': 'ghi ', '5': 'jkl ', '6': 'mno ', 
        '7': 'pqrs', '8': 'tuv ', '9': 'wxyz'}
output = {}
digits = '23'

for digit in digits:
    #print(list(enumerate(MAP[digit])))
    for idx, value in enumerate(MAP[digit]):
        print(MAP[digit][idx])
        for digit in digits:
            output[digit] = output.get(digit, "") + MAP[digit][idx]
        


'''
output = [MAP[digit][index] for digit in digits
                             for index, letter in enumerate(MAP[digit])]
'''
print(output)