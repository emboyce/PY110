def parts(string):
    word_list = []
    counter = 1
    while counter <= len(string):
        word_list.append(string[:counter])
        counter += 1
    return word_list

word = 'Sesquipedalianism'
print(parts(word))  # ['S', 'Se', 'Ses', 'Sesq', 'Sesqu', 'Sesqui', 'Sesquip', 'Sesquipe', ...]

def largest_column(arrays):
    column_count = len(arrays[0])
    max_sum = 0
    max_list = []
    column = 0

    while column < column_count:
        for subarray in arrays:
            max_sum += subarray[column]
        max_list.append(max_sum)
        max_sum = 0
        column += 1

    return max(max_list)

a = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

b = [[1, 2, 3, 4],
    [5, 6, 7, 8]]

c = [[1, 0, 0],
     [5, 8, 10],
     [3, 5, 1]]

print(largest_column(a) == 18)
print(largest_column(b) == 12)
print(largest_column(c) == 13)