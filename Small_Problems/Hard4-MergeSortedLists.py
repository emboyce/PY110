'''
Compare the first value in each list. Take the lower one.
'''

def merge(lst1, lst2):
    l1 = lst1.copy()
    l2 = lst2.copy()
    output = []
    while l1 and l2:
        if l1[0] < l2[0]:
            output.append(l1.pop(0))
        else:
            output.append(l2.pop(0))
    
    if l1:
        output.extend(l1)
    if l2:
        output.extend(l2)

    return output

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
print(names1, names2)