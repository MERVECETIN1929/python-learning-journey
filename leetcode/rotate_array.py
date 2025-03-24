class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #kaç birim kaydıracağımız bilgisini taşıyan k değeri diziden büyük olması durumunda gereksiz işlem yapılır
        n=len(nums)
        k=k%n
        #öncelikle tüm listeyi baştan sona ters çevirip sonrasında ikiye bölüp tekrar ters çevireceğiz
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        print(nums)
solution = Solution()
solution.rotate(nums=[-1, -100, 3, 99], k=2)
solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
