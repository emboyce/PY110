'''
add 1 1 to an array
then each later array member is the sum of the previous two
'''

def fibonacci(num):
    fib = [1, 1]

    if num > 1:
        for _ in range(num - 2):
            fib.append(fib[-1] + fib[-2])

    return fib[num - 1]

print(fibonacci(6))

def fib_recursive(num):
    if num == 2:
        return 1
    elif num == 1:
        return 1
    else:
        return fib_recursive(num - 1) + fib_recursive(num - 2)
    
print(fib_recursive(20))
    
arr = {1: 1, 2: 1,}
def fib_memo(num):
    if num in arr:
        return arr[num]
    else:
        arr[num] = fib_memo(num - 1) + fib_memo(num - 2)
        return arr[num]
    

print(fib_memo(12))
print(len(list(str(fib_memo(12)))))

def find_fibonacci_index_by_length(l):
    num = 1
    while len(str(fib_memo(num))) < l:
        num += 1
    return num

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
#print(find_fibonacci_index_by_length(10000) == 47847)