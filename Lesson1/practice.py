fruits = ("apple", "banana", "cherry", "date", "banana")

print(fruits.count("banana"))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.union(b)
d = a | b
print(d)

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

sum_ages = sum((ages.values()))
print(sum_ages)

min_age = min(ages.values())
print(min_age)

statement = "The Flintstones Rock"
#statement = "".join(statement.split())
statement = statement.replace(" ", "")

dict_statement = {}
two_dict_statement = {}
for char in statement:
    # dict_statement[char] = statement.count(char)
    dict_statement[char] = dict_statement.get(char, 0) + 1
    two_dict_statement[char] = statement.count(char)

print(dict_statement == two_dict_statement)