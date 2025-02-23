matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_matrix = [num for list in matrix
                        for num in list]

print(flattened_matrix)

print("flattened_duplicates")

def remove_duplicates(my_list):
    list_ = []
    result = [list_.append(num) for num in my_list if (num not in list_)]
    return list_

dup_list = [1, 2, 3, 1, 2, 4, 5]
print(remove_duplicates(dup_list))  # => [1, 2, 3, 4, 5]

print("Shannon practice")

message = 'Please call me at five, five !five! one two three four?'

def alpha(a_word):
    str_ = ""
    for char in a_word:
        if char.isalpha():
            str_ += char 
    return str_

def word_to_digit(phrase):
    num_words = {
                "zero": "0",
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9",
    }
    lst_msg = phrase.split()
    num_msg = []
    for word in lst_msg:
        if alpha(word) in num_words.keys():
            num_msg.append(word.replace(alpha(word), num_words[alpha(word)]))
        else:
            num_msg.append(word)
    return " ".join(num_msg)
    

print(word_to_digit(message))