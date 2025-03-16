class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2  # Listeleri birleştir
        nums.sort()  # Listeyi sırala
        size = len(nums)  # Listenin uzunluğunu al

        if size % 2 == 0:  # Eğer eleman sayısı ÇİFT ise
            total = (nums[size//2] + nums[(size//2)-1]) / 2.0
            return float(total)
        else:  # Eğer eleman sayısı TEK ise
            return float(nums[size//2])  # Ortadaki elemanı döndür


solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
