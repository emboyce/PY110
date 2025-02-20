def is_real_palindrome(string):
    clean_string = ""
    for char in string:
        if char.isalnum():
            clean_string += char.lower()

    return is_palindrome(clean_string)

def is_palindrome(string):
    return string == string[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True