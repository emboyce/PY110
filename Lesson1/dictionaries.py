dictio = {"one": "chicken","two": "lizard",}
dictio2 = {dictio["two"]: "pig"}
print(dictio2["lizard"])

dictio3 = {"pear": "fruit", "broccoli": "Vegetable",}
dictio["pear"] = "fruit"
dictio["broccoli"] = "Vegetable"

listio = [[1,2], [2,3]]
print(dict(listio))
print(dict(listio)[1])

lista = [5, 4, 3, 2]
enumo = enumerate(lista)
print(dict(enumo))

rango = range(5)
print(rango.count(5))
print(5 in rango)

string = "This is the first line.\nThis is still the first line.\nThis is the second line."
cleaned_string = string.replace("\n", " ", 1)
print(cleaned_string)
# 'This is the first line. This is still the first line.\nThis is the second line.'

print('Straße'.swapcase())
print('Straße'.casefold().swapcase())
print('Straße'.lower().upper())

numbers = [1, 2, 3, 4, 5]
hat = (str(number) for number in numbers)
print(hat)
print('-'.join(hat))

hat = [str(number) for number in numbers]
print(hat)

print(str(frozenset([1, 2, 3])))

listy = [1, "!"]
listy.sort(key=str)
print(listy)

x, y, z = (1, 2, 3)
print(x)

dicto = {"country": "Romania"}
temp = dicto.setdefault("country", "Rossland")
print(temp)