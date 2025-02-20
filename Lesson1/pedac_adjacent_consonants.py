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
- it's bad practice to mutate the original list while incrementing through it, so I'm going to create a new list
- initialize a new shallow copy list variable
    - this will contain the strings in the original order, prepended by a number 
- initialize a consonant counter variable

    ABANDONING THIS NOW THAT I KNOW TO USE THE KEY PART OF SORT. THIS IS VERY SCRAPPY.


'''
alist = ["123b", "42a", "123b"]
alist.sort()
print(alist)

def sort_by_consonant_count(strings):
    pass
    

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