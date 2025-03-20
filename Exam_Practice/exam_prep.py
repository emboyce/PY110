d1 = {"a": 1, "b": 2,}
x = all(d1)

print(x)

def slower(str):
    return str[-1]
    

animals = ['Cat', 'dog', 'ZEBRA', 'monkey']
sorted_animals = sorted(animals, key=slower)
print(sorted_animals)
# Expected output: ['Cat', 'dog', 'monkey', 'ZEBRA']
# Actual output:   ['Cat', 'ZEBRA', 'dog', 'monkey']

dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

print(list(dict2['3rd'].keys())[0])

lst = [[1], [2]]

lst[0].append([9])
print(lst[0][1][0])                 # [[1, [9]], [2]]

a = [1, 3]
b = [2]
lst = [a, b]

print(lst)          # [[1, 3], [2]]

a[1] = 5
print(lst)          # [[1, 5], [2]]
a = [4, 5]
print(lst)

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
#[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
d = {'d': 4, 'e': 5, 'f': 6}
print(d.items())

lst2 = [{key: (value + 1) for key, value in dict.items()} for dict in lst]
print(lst2)

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def div3(lst):
    output = []
    for item in lst:
        if item % 3 == 0:
            output.append(item)
    return output

lst2 = [div3(arr) for arr in lst]
print(lst2)

import random

lst = [8, 4, 4, 4, 12]
digits = list(str(1234567890)) + list('abcdef')
output = ""
for num in lst:
    while num > 0:
        output += digits[random.randint(0, 15)]
        num -= 1
    output += "-"
print(output[:-1])

def makestring(num):
    output = ""
    while num > 0:
        output += digits[random.randint(0, 15)]
        num -= 1
    return output

output = "-".join([makestring(num) for num in lst])
print(output)

s = {(1, 2)}
print(1 in s)

c = ['c', 'd']
e = [1, 2]
f = list(zip(c, e))
print(f)
g = dict(f)
print(g)

apple = "apple"

pear = list(apple)

def test(num, lst=None):
    if lst == None:
        lst = []
    return lst

print(test(2))

print(apple.index("l"))


def center_of(phrase):
    mid = len(phrase) // 2
    if len(phrase) % 2 == 0:
        return phrase[mid - 1 : mid + 1]
    else:
        return phrase[mid]


print(center_of('I Love Python!!!'))# == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True

def word_strings(word):
    output = [word[start:stop + 1] for start in range(len(word))
                               for stop in range(len(word))
                               if len(word[start:stop + 1]) > 1]
    return output

def palindromes(word):    
    return [sub for sub in word_strings(word)
                    if sub == sub[::-1]]

print(palindromes('madam')) == ['madam', 'ada']   # True
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes')==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True


def clean_up(str):
    output = ""
    for char in str:
        if char.isalpha():
            output += char
        else:
            if output.endswith(" "):
                continue
            else:
                output += " "
    return output
        
print(clean_up("---what's my +*& line?") == " what s my line ")
