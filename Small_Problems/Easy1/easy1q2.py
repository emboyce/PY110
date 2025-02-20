# All of these examples should print True

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)