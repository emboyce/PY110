from datetime import date
#Monday is 0, Friday is 4


def friday_the_13ths(year):

    fri_13 = 0

    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            fri_13 += 1

    return fri_13

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True