def twoSum(nums):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    output = set()
    for i in range(len(nums) + 1):
        for j in range(i + 1, len(nums) + 1):
            print([i, j], nums[i:j])
            output.add(nums[i:j])
    
    print(output)

twoSum([2,7,11,15])