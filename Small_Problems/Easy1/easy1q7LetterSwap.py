'''
P/E:
Input: a string of words separated by spaces
Output: a string of words in which the first and last letters of every word have been swapped
Rules explicit:
- every word contains 1+ letters, every string contains 1+ words
- each string contains only words and spaces
- no leading, trailing or repeated spaces
Rules implicit:
- no no-alpha characters
- may contain capitals
'''
def swap(phrase):
    word_list = phrase.split()
    for index, word in enumerate(word_list):
        if len(word) > 1:
            word_list[index] = word[-1] + word[1:-1] + word[0]
    return " ".join(word_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True