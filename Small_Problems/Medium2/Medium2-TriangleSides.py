def triangle(s1, s2, s3):
    sides = sorted([s1, s2, s3])

    l1, l2, l3 = sides

    if (l1 + l2) < l3 or 0 in sides:
        return "invalid"
    elif l1 == l2 and l2 == l3:
        return "equilateral"
    elif l1 == l2 or l2 == l3:
        return 'isosceles'
    else:
        return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

print("q3")

def triangled(*d):
    if 0 in d or sum(d) != 180:
        return 'invalid'
    elif any(deg == 90 for deg in d):
        return 'right'
    elif all(deg < 90 for deg in d):
        return 'acute'
    else:
        return 'obtuse'
    

print(triangled(60, 70, 50) == "acute")      # True
print(triangled(30, 90, 60) == "right")      # True
print(triangled(120, 50, 10) == "obtuse")    # True
print(triangled(0, 90, 90) == "invalid")     # True
print(triangled(50, 50, 50) == "invalid")    # True