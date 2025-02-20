"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""
def palindrome_substrings(string):
    pal_set = set()
    step_index = 1
    for index, char in enumerate(string):
        try:
            if char == string[index+1]:
                pal_set.add(char * 2)
                while string[index - step_index] == string[index + step_index + 1]:
                    pal_set.add(string[index - step_index:index + step_index + 2])
                    step_index += 1
                step_index = 1
            else:
                while string[index - step_index] == string[index + step_index]:
                    pal_set.add(string[index - step_index:index + step_index + 1])
                    step_index += 1
                step_index = 1
        except IndexError:
            step_index = 1
    print(list(pal_set))
# Test cases:

palindrome_substrings("cabac")
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]


# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]
