def differenceOfTwo0(arr):
    output = []
    arr_sorted = sorted(arr)

    for num1 in arr_sorted:
        for num2 in arr_sorted[1:]:
            if num2 - num1 == 2:
                output.append([num1, num2])
            continue

    return output

def differenceOfTwo1(lst):
    a = [[b, a] for a in lst for b in lst if (a - b) == 2]
    print(a)
    return a

def differenceOfTwo2(arr):
    output = []
    arr_sorted = sorted(arr)

    for idx, num in enumerate(arr_sorted):
        print(arr_sorted[idx + 1: idx + 3])
        if (num + 2) in arr_sorted[idx + 1: idx + 3]:
            output.append([num, num + 2])
    
    return output

def differenceOfTwo(arr):
    arrs = sorted(arr)
    output = [[num, num + 2] for idx, num in enumerate(arrs) 
                             if num + 2 in arrs[idx + 1: idx + 3]]
    return output

print(differenceOfTwo([1, 2, 3, 4]) == [[1, 3], [2, 4]])
print(differenceOfTwo([4, 1, 2, 3]) == [[1, 3], [2, 4]])
print(differenceOfTwo([1, 23, 3, 4, 7]) == [[1, 3]])
print(differenceOfTwo([4, 3, 1, 5, 7]) == [[1, 3], [3, 5], [5, 7]])
print(differenceOfTwo([2, 4]) == [[2, 4]])
print(differenceOfTwo([1, 4, 7, 10, 13]) == [])