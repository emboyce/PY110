def merge(lst1, lst2):
    l1 = lst1[:]
    l2 = lst2[:]
    output = []

    while l1 and l2:
        if l1 < l2:
            output.append(l1.pop(0))
        else:
            output.append(l2.pop(0))

    return output + l1 + l2

'''
- break the list into two sub-lists
    - [0:len/2], [len/2:]
- continue to do this until the length of the sub-lists is 1
- merge the sub-lists, which also recombines them
'''

'''def split(lst):
    half = len(lst) // 2
    split_lst = [lst[:half], lst[half:]]
    print(split_lst)'''

def merge_sort(lst):
    half = len(lst) // 2
    if half == 0:
        return lst

    return merge(merge_sort(lst[:half]), merge_sort(lst[half:]))

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)