class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        check_char = set()
        for char in s:
            if not (char in check_char) and s.count(char) != t.count(char):
                return False
            else:
                check_char.add(char)
        return True


solution = Solution()
print(solution.isAnagram("rat", "iar"))
