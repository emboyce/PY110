def length(word):
    word_length = 0
    for char in word:
        if char.isalpha():
            word_length += 1
    return word_length


def word_sizes(phrase):
    words = phrase.split()
    counts = {}
    for word in words:
        counts[length(word)] = counts.setdefault(length(word), 0) + 1
    print(counts)
    return counts



# All of these examples should print True
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty humpty sat on a w@ll'
print(word_sizes(string) == {6: 3, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
