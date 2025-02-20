'''
P/E:
Input - list of strings
Output - sorted list of strings, sorted by highest number of adjacent consonants
Rules (explicit):
- if two strings contain the highest number of adjacent consonants (AC), they should retain their original order
- consonants are adjacent if they're next to one another in a word OR if there's a space between consonants in adjacent words
Rules (implicit):
- zero length string? -> No
- language? -> english
- case sensitive? -> No
- ok to return a new object? -> Yes
- strings may contain more than one word -> yes
- sort order ascending or descending? -> most consonants first
New Rules:
- consonants don't have to be the same consonant, just any consonant
- single consonants don't count and maintain the same order as zero consonants
D/A:
    - helper function - consonant_counter
        - strip spaces, convert to list
        - set max consonants to 1
        - set consonant counter to 0
        - while list has length:
            - pop last list element
            - if not in vowels, increment consonant counter
            - repeat until in vowels
            - then compare consonant counter to max and set max to highest of the two
        - return max consonants
    
    - sort the original array on the key of consonant_counter


    ccc
    c
    cc
    ccc
    end

    cccaccc
    c
    cc
    ccc
    ccca -> false

    # bbb 0, b/bb +1 , b/b +2, b/[] +3


'''
def sort_by_consonant_count(strings):
    strings.sort(key=consonant_counter, reverse=True)
    return strings

#This is the second cleaner version which improves on the official solution, noting that looking at the letter
#   itself instead of the next letter is much more straightforward, resetting the count when a vowel is encountered 
def consonant_counter(string):
    char_str = "".join(string.split())
    max_consonants = 0
    consonants = 0
    vowels = "aeiou"
    for char in char_str:
        if char not in vowels:
            consonants += 1
            max_consonants = max(max_consonants, consonants)
        else:
            max_consonants = max(max_consonants, consonants)
            consonants = 0

    if max_consonants == 1:
        return 0
    else:
        return max_consonants

#This was the first attempt and is unnecessarily complicated
def consonant_counter1(string):
    char_list = list("".join(string.split()))
    max_consonants = 0
    vowels = "aeiou"
    while len(char_list) > 0:
        consonants = 0
        try:
            while char_list.pop() not in vowels:
                consonants += 1
        except IndexError:
            pass
        max_consonants = max(consonants, max_consonants)
    if max_consonants == 1:
        return 0
    else:
        return max_consonants

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

