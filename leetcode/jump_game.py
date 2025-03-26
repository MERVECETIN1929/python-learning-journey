class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # En uzak noktayı başlangıçta 0 olarak belirle
        max_reach = 0

        # Dizi boyunca gezin
        for i in range(len(nums)):
            # Eğer i'ye kadar olan mesafeye sıçrayamazsak, False döndür
            if i > max_reach:
                return False

            # Şu anki konumdan ne kadar ileriye sıçrayabileceğimizi hesapla
            max_reach = max(max_reach, i + nums[i])

            # Eğer en uzak noktaya dizinin sonu ulaşabiliyorsa, True döndür
            if max_reach >= len(nums) - 1:
                return True

        # Eğer döngü tamamlanırsa ve dizinin sonuna ulaşamadıysak, False döndür
        return False


solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))
print(solution.canJump([3, 2, 1, 0, 4]))
print(solution.canJump([0]))
print(solution.canJump([2, 0, 0]))
print(solution.canJump([1, 1, 1, 1, 0]))
print(solution.canJump([3, 0, 8, 2, 0, 0, 1]))
print(solution.canJump([1, 1, 0, 1]))
print(solution.canJump([1, 1, 2, 2, 0, 1, 1]))
