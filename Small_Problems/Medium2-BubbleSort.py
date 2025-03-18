def bubble_sort(arr):
    
    while True:
        yes_swap = False

        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx + 1], arr[idx] = arr[idx], arr[idx + 1]
                yes_swap = True

        if yes_swap == False:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True