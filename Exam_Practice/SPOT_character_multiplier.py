'''
P:
Input = a string and an integer with the same number of digits as the string
Output = a string where the characters have been multiplied by the digit
Rules:
- capitalize all instances of a letter if the multiplier for that letter is ever over 3
- no funny business (empty strings, non-alpha chars, etc)
D:
- first build a set of characters to uppercase
- initialize a set for uppercase characters
- convert the input string to a list
- convert the ROM to a list of integers
    - use a list constructor and str and int conversions
    - enumerate over the list of characters
        - if the multiplier list at that index is over 3, add the character to the uppercase set
- for each letter in the list, check whether it's in the uppercase set
    - if yes, uppercase it
    - if no, don't change it
- at the same time, enumerate over the list of characters and mutate it so that the characters are multiplied
    - for index, char in list
        - char *= multiplier list [index]
- convert the list back to a string
- return the string
'''

def multiplicity(string, multiplier):
    up_set = set()
    s_list = []
    s_list += string
    m_list = [int(num) for num in str(multiplier)]
    
    for index, s in enumerate(s_list):
        if m_list[index] > 3:
            up_set.add(s)

    for index, s in enumerate(s_list):
        if s in up_set:
            s_list[index] = s.upper() * m_list[index]
        else:
            s_list[index] = s * m_list[index]

    m_string = "".join(s_list)
    return(m_string)

multiplicity("aabac", 42354)