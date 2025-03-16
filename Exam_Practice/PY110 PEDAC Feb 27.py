import pdb

'''Initialize an empty list
Loop from idx length - 1 to zero (inclusive)
	Integer divide the number by 10**idx
	Store the result in the list
	Subtract the result from the number
	Stop when idx is zero (or when number is zero)
Join the list into a string using the "+" 
Return the string'''
pdb.set_trace()

def expanded_form(num):
    result = []
    for idx in range(len(str(num)) - 1, -1, -1):
        div_result = num // 10**idx
        div_result *= 10**idx
        if div_result:
            result.append(str(div_result))
        num = num - div_result
    return " + ".join(result)

print(expanded_form(12) == '10 + 2')
print(expanded_form(42) == '40 + 2')
print(expanded_form(70304) == '70000 + 300 + 4')

'''
Compare 2 digits - if the leading one is greater, drop the next one.
Continue through string.

Compare int digits at two indices
 - convert number to string
 - convert str_digit to int to compare
 If lower index one is smaller, remove that one
 Continue to end (range 0 to len - 1)
'''
print("delete digit")
def delete_digit(num):
    str_num = str(num)
    for idx in range(len(str_num) - 1):
        if str_num[idx] < str_num[idx + 1]:
            str_num = str_num[:idx] + str_num[idx+1:]
            return int(str_num)
    return int(str_num[:-1])
        
print(delete_digit(791983) == 91983)
print(delete_digit(152) == 52)
print(delete_digit(1001) == 101)
print(delete_digit(10) == 1)