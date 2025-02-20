def running_total(nums):
        totals = []
        for index, _ in enumerate(nums):
            totals.append(sum(nums[0 : index + 1]))
            print(index, totals)
        return totals
    
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True