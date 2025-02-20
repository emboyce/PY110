produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit1(veggies):
    fruit_dicts = {}
    for key, value in veggies.items():
        if value == 'Fruit':
            fruit_dicts[key] = value
    return fruit_dicts

def select_fruit(veggies):
    fruit_dicts = {}
    for item in veggies:
        print(item)
        if veggies[item] == "Fruit":
            fruit_dicts[item] = veggies[item]
    return fruit_dicts

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

print("new")

my_numbers = [1, 4, 3, 7, 2, 6]

def double_numbers(nums):
    for index, num in enumerate(nums):
        nums[index] = num * 2
    return nums

print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [1, 4, 3, 7, 2, 6]

print("new")

my_numbers = [1, 4, 3, 7, 2, 6]

def double_odd_numbers(nums):
    numbers = nums.copy()
    for index in range(1, len(nums), 2):
        numbers[index] = nums[index]*2
    return numbers
                       
                       
print(double_odd_numbers(my_numbers))  # [2, 4, 6, 14, 2, 6]

# not mutated
print(my_numbers)                      # [1, 4, 3, 7, 2, 6]

print("new")

my_numbers = [1, 4, 3, 7, 2, 6]
def multiply(nums, multiplier):
    new_nums = []
    for num in nums:
        new_nums.append(num * multiplier)
    return new_nums

print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]