def integer_to_string(num):
    str_num = ""

    while num > 0:
        digit = num % 10
        str_num = chr(digit + 48) + str_num
        num = num // 10

    return str_num or "0"

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

'''
ord(0) = 48
chr(num + 48) = string value
integer % 10 = remainder last place

4321
4321 % 10 = 1
4321 // 10 = 432

digit is num % 10
remainder is num // 10

pull out digit with num %10
add digit to string
convert num to remainder with num // 10
'''
