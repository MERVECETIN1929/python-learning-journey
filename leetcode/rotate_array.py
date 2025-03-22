class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        for i in range(k):
            for i in range(len(nums)-1, 0, -1):
                nums[i], nums[i-1] = nums[i-1], nums[i]
        print(nums)


solution = Solution()
solution.rotate(nums=[-1, -100, 3, 99], k=2)
solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
