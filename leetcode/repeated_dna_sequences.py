class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        all_subset_dna = list()
        more_list = set()
        for i in range(0, len(s)-9):
            all_subset_dna.append(s[i:i+10])

        for i in all_subset_dna:
            if all_subset_dna.count(i) > 1:
                more_list.add(i)

        return list(more_list)


solition = Solution()
print(solition.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        result = set()

        for i in range(len(s) - 9):  # i, 0'dan len(s)-10'a kadar gider
            tmp = s[i:i+10]
            if tmp in seen:
                result.add(tmp)
            seen.add(tmp)

        return list(result)
