lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst2 = sorted(lst)
print(lst2)

lst3 = sorted(lst, reverse=True)
print(lst3)

print("q2")

lst.sort(reverse=True)
print(lst)

print("q3")
lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst.sort(key=str, reverse=True)
print(lst)

print("q4")
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def by_year(dicto):
    year = dicto["published"]
    return int(year)

books.sort(key=by_year)
print(books)