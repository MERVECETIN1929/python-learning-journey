class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicates = False
        i = 0
        current_len = len(nums)
        while i < current_len-1:
            if nums[i] == nums[i+1] and not duplicates:
                duplicates = True
            elif nums[i] == nums[i+1] and duplicates:
                nums.pop(i+1)
                i = i-1
                current_len -= 1
            if nums[i] != nums[i+1]:
                duplicates = False
            i = i+1
        return len(nums)


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))
