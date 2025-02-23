lst = [340, 15, 1, 3400]
lst1 = ["aa", "a", "bc", "Abc"]

lst.sort()
print(lst)             # [1, 15, 340, 3400]

lst1.sort()
print(lst1)            # ['Abc', 'a', 'aa', 'bc']

DATA = [
    {'one': '1', 'two': 2},
    [{'four': 5, 'three': 6}, 'three'],
    'three',
    {'2': 'two', '3': 'three'}
]
print(DATA[1][0]['three'])

todo_lists = [
    {
        "id": 1,
        "list_name": 'Groceries',
        "todos": [
            {"id": 1, "name": 'Bread', "completed": False},
            {"id": 2, "name": 'Milk', "completed": False},
            {"id": 3, "name": 'Apple Juice', "completed": False}
        ]
    }
]
todo_lists[0]['todos'][2]["name"] = "OJ"
print(todo_lists[0]['todos'][2])

def even_values(lst):
    evens = []

    for value in lst:
        if value % 2 == 0:
            evens.append(value)
        lst.pop(0)

    return evens

print(even_values([1, 3, 4, 2, 4, 6, 5, 7, 9, 10, 12]))

lst = [1, 2, [3,4]]
print(type(lst.pop()))
lst2 = sorted(lst)
print(lst2 is lst)