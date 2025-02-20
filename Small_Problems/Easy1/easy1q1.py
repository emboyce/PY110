
# Q1
nums = []
for index in range (1, 6):
    nums.append(input(f"Enter number {index}:"))
check = input("Enter the last number:")
if check in nums:
    print(f"{check} is in {",".join(nums)}")
else:
    print(f"{check} isn't in {", ".join(nums)}")
