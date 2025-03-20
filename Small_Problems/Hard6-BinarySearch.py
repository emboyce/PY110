'''
retrieve the middle item from the list
check if the item is equal to the search key
if yes, stop the search and return the index found at
if no, check if < middle value
split list accordingly
repeat on the original part of the list
if the list length is 1 and the value is not the search key, return -1

'''

def binary_search(arr, search):
    if arr[0] == search:
        return 0
    
    low_idx = 0
    high_idx = len(arr)
    while len(arr[low_idx:high_idx]) > 1:
        #print(arr[low_idx:high_idx])
        #p = input("next")
        middle_idx = len(arr[low_idx:high_idx]) // 2
        if arr[low_idx + middle_idx] == search:
            return low_idx + middle_idx
        elif arr[low_idx + middle_idx] < search:
            low_idx += middle_idx
        else:
            high_idx -= middle_idx
    return -1

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Apple Store') == 0)


print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search([77, 5, 7, 11, 23, 65, 89, 102], 77) == 0)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)
'''
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)

len = 8
mid = 3

len = 4
mid = 1

len = 2
mid = 0

mid(0) = thing

index = 6


'''