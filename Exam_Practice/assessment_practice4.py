'''
Practicing Substrings and Filtering

- out - all including repeating sub-strings of a phrase
A:
- two indices, slice from first index to second index
    - first index starts at zero
    - second index starts at i + 1
    - first index ends at len(str) - 1
    - second index ends at len(str)
    - so RANGE is i = (1, len(str))
                  j = (i + 1, len(str) + 1)

'''
def low_help(arr):
    for item in arr:
        if not item.islower():
            return None
    return arr

def substrings(phrase):
    subs = [low_help(phrase[i:j]) for i in range (0, len(phrase))
                        for j in range(i + 1, len(phrase) + 1)]
    subs_real = [item for item in subs if not item == None]
    print(subs_real)

substrings('abcD')


s = "hih"
s = s.replace("h", "H", 1)
print(s)
print(s.count("H", 4))
l = [1, 2]
print(l.count(1))
print(l.find(1))

phrase = "heLlo"
output = []

def is_lower(arr):
    for item in arr:
        if not item.islower():
            return False
    return True


for i in range(len(phrase)):
    for j in range(i + 1, len(phrase) + 1):
        if is_lower(phrase[i:j]):
            output.append(phrase[i:j])

print(output)