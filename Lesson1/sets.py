fruits1 = {'apple', 'banana'}
fruits2 = {'cherry', 'date'}
fruits3 = {'apple'}
fruits4 = {'banana', 'cherry'}
fruits5 = {"apple", "banana", "cherry"}

print(fruits3.issuperset(fruits5))
print(fruits3.issubset(fruits5))

fruits6 = fruits2.copy()
fruits6.add("snake")
print(fruits2, fruits6)

list1 = ["cat"]
list2 = list1.copy()
list2.append("dog")
print(list1, list2)

