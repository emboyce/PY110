from pprint import pprint

'''
P:
in: list of ints between 0 and 19
out: list of those ints sorted by the english word for each number
Sort integers in a list by the english word representing the integer
E:
- all integers, no edge cases
- integers list is ordered and begins with 0
- no duplicates
'''

def alphabetic_number_sort0(nums):
    num_names = ["zero", "one", "two", "three", "four", "five", 
                 "six", "seven", "eight", "nine", "ten", "eleven", 
                 "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                 "seventeen", "eighteen", "nineteen"]
    num_dict = {name:index for index, name in enumerate(num_names)}
    order_list = sorted(num_names)

    result = [num_dict[element] for element in order_list]

    return result

NUM_NAMES = ["zero", "one", "two", "three", "four", "five", 
            "six", "seven", "eight", "nine", "ten", "eleven", 
            "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]
def sorter_fun(num):
    return NUM_NAMES[num]

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print([sorter_fun(num) for num in input_list])

def alphabetic_number_sort(nums):
    nums_sorted = sorted(nums, key=sorter_fun)
    print(nums_sorted)
    return nums_sorted

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

print("q2")

def merge_sets(lst1, lst2):
    return set(lst1) | set(lst2)
    #return set(lst1).union(set(lst2))
list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

print("q3")

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})

def intersection(lst1, lst2):
    fr1, fr2 = frozenset(lst1), frozenset(lst2)
    return fr1 & fr2
print(intersection(list1, list2) == expected_result) # True

print("q4")

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']

def key_valuer0(a_key):
    return my_dict[a_key]

def order_by_value0(dicto):
#    return sorted(dicto.keys(), key=key_valuer)
    return sorted(dicto.keys(), key=dicto.get)

def key_valuer(item):
    return item[1]

def order_by_value(dictionary):
    sorted_items = sorted(dictionary.items(), key=key_valuer)
    return [key for key, item in sorted_items]

print(order_by_value(my_dict) == keys)  # True

print("q5")

def unique_from_first(lst1, lst2):
    return set(lst1) - set(lst2)
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

print("q6")
def leading_substrings(string):
    return [string[:index + 1] for index in range(len(string))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

print("q7")

def substrings0(string):
    sub_list = []
    for idx in range(len(string)):
        sub_list += leading_substrings(string[idx:])
    print(sub_list)

def substrings1(string):
    sub_list = [leading_substrings(string[idx:]) for idx in range(len(string))]
    return [str for sub in sub_list
                for str in sub]

def substrings(string):
    return [leading_substring
            for idx in range(len(string))
            for leading_substring in leading_substrings(string[idx:])]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]
print(substrings('abcde'))
print(substrings('abcde') == expected_result)  # True

print("q8")

def palindromes(string):
    result = [substring for substring in substrings(string) 
                        if substring == substring[::-1]
                        and len(substring) > 1]
    return result

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

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

print("q9")

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]


def transactions_for(item_id, transactions):
    return [dictionary for dictionary in transactions
                       if dictionary["id"] == item_id]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

print("q10")

def is_item_available(item_id, transactions):
    item_transactions = transactions_for(item_id, transactions)
    items_on_hand = sum([transaction["quantity"]
                         if transaction["movement"] == "in"
                         else -transaction["quantity"] 
                            for transaction in item_transactions])
    return items_on_hand > 0

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True