def integer_to_string(num):
    str_num = ""
    num = abs(num)

    while num > 0:
        digit = num % 10
        str_num = chr(digit + 48) + str_num
        num = num // 10

    return str_num or "0"

def signed_integer_to_string(signed_num):
    result = integer_to_string(signed_num)
    if signed_num < 0:
        return "-" + result
    elif signed_num == 0:
        return result
    else:
        return "+" + result


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

