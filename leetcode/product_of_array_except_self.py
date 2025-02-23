class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()
        carpma = 1
        sifir_index = int()
        if 0 in nums:
            sifir_index = nums.index(0)
            for i in range(len(nums)):
                if sifir_index == i:
                    continue
                carpma = carpma * nums[i]
            for i in range(len(nums)):
                if i != sifir_index:
                    result.append(0)
                else:
                    result.append(carpma)
        else:
            for i in nums:
                carpma = carpma * i
            for i in nums:
                result.append(carpma/i)
        return result


solution = Solution()
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
