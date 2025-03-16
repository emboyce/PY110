'''
P:
input: a pos or neg number of minutes
output: time in a 24-hr string format, xx:xx
rules:
- E - works with any integer input, including zero
- E - may not use datetime
- E - disregard DST etc
D/A:
- first, store the sign of the integer
- can treat zero like a positive
- reduce minutes until they're less than a day
- convert to hours and minutes (discard seconds)
- add or subtract from midnight

'''
MINS_IN_DAY = 60 * 24
MINS_IN_HR = 60

'''def fill(time):
    if time == 0:
        return "00"
    elif len(str(time)) >= 2:
        return str(time)
    else:
        return "0" + str(time)'''

def time_of_day(minutes):
    abs_minutes = abs(minutes)
    
    while abs_minutes > MINS_IN_DAY:
        abs_minutes -= MINS_IN_DAY

    if minutes < 0:
        time = MINS_IN_DAY - abs_minutes
    else:
        time = abs_minutes

    hours = time // MINS_IN_HR
    mins = (time - (hours * MINS_IN_HR))

    return f"{hours:02d}:{mins:02d}"


print(time_of_day(3000) == "02:00")     # True
print(time_of_day(-3) == "23:57")       # True

print(time_of_day(0) == "00:00")        # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

print("q2")

def after_midnight(time):
    hours = int(time[:2])
    mins = int(time[-2:])
    duration = hours*MINS_IN_HR + mins
    if duration == MINS_IN_DAY:
        return 0
    else:
        return duration

def before_midnight(time):
    duration_after = MINS_IN_DAY - after_midnight(time)
    if duration_after == MINS_IN_DAY:
        return 0
    else:
        return duration_after

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

'''
After:
Calculate the number of minutes
If the number of minutes is equal to the number of minutes in a day, return 0
Before:
Calculate the minuer of minutes
Subtract it from the number of minutes in a day
'''

print("q3")
'''
in: str
out: str, all chars doubled. Yes empty strs.
list comprehension...I think this will work naievely for empty strs
'''
def repeater(phrase):
    phrase_doubled = [char * 2 for char in phrase]
    return "".join(phrase_doubled)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

print("q4")
'''
in: str
out: str with non-vowel letters doubled and everything else as it was
list comprehension
check if not vowel and yes alpha, if yes double, otherwise add once
'''

def double_consonants(phrase):
    semi_doubled = [(char*2 if char.isalpha() 
                            and char not in "aeiouAEIOU"
                            else char) for char in phrase]
    return "".join(semi_doubled)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

print("q5")
'''
in: positive integer
out: number with digits reversed
rules:
- 1 digit returs same
- leading zeroes in return string get deleted
    - so you can use int conversion on it to return without trouble
'''
def reverse_number(num):
    return int(str(num)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

print("q6")

'''
in: positive, non-zero integer argument
out: list containing all ints between 1 and the argument, inclusive, in ascending order
list comprehension over a range, inclusive
'''
def sequence(num):
    return [num for num in range(1, num + 1)]

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

print("q7-8")
'''
in: str, first - space - last
out: str, last, comma, first
'''
def swap_name(name):
    outname = ", ".join(name.rsplit(" ", 1)[::-1])
    return outname

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True

print("q9")
'''
in: integer count, integer starting number of sequence
out: list with count number elements, each element is a multiple of the starting number
rules:
- count integer, >= 0
- starting number can be any integer, pos or negative
- if count is zero, should return an empty list
plan:
iterate over range from 1 to count(+1). Add element to list that's starting number * range index.
4 -7
range: (1, 5)
1, 2, 3, 4
1*-7 = 14, 2*-7 = -14, 3*-7 = ...

'''
def sequence(count, start):
    output = [index * start for index in range(1, count + 1)]

    return output

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

print("q10")

'''
in: list
out: list, reversed in place (in is out)
- may not use slice or list.reverse
1, 2, 3, 4
0, 1, 2, 3

2, 3, 4, 1
0, 1, 2, 3

FILO stack

1, 2, 3, 4 (append)
4, 3, 2, 1 (pop)

FILO to new list and back to old list with pop and append
'''

def reverse_list(input):
    stack = []
    while len(input):
        stack.append(input.pop(0))
    while len(stack):
        input.append(stack.pop())
    return input

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

print("q10v2")

def reverse_nopop(input):
    idx = 0
    while idx < len(input) // 2:
        input[idx], input[-(idx + 1)] = input[-(idx + 1)], input[idx]
        idx += 1
    return input

list1 = [1, 2, 3, 4]
result = reverse_nopop(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

print("q11")

def is_balanced(string):
    par_list = [char for char in string if char == "(" or char == ")"]

    par_count = 0
    for par in par_list:
        if par_count < 0:
            return False
        if par == "(":
            par_count += 1
        elif par == ")":
            par_count -= 1
    
    return par_count == 0

print(is_balanced("((What) (is this))?"))
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

