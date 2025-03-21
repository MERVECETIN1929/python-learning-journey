class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        have_number = set()
        for number in nums:
            if number not in have_number:
                if nums.count(number) > len(nums)/2:
                    return number
                have_number.add(number)


solution = Solution()
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(solution.majorityElement([1, 3, 2, 3, 2, 3, 3]))
