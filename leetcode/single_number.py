def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]


list1 = [1, 1, 2, 2, 5, 5, 10]
print(singleNumber(list1))
