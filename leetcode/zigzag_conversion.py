from functools import reduce


class Solution:
    def convert(self, s, numrows):
        if len(s) < numrows or numrows == 1:
            return s

        store_string = [""]*numrows
        index, step = 0, 1
        for letter in s:
            store_string[index] += letter
            if index == 0:
                step = +1
            elif index == numrows-1:
                step = -1
            index += step
        return "".join("".join(line) for line in store_string)


solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))
print(solution.convert("PAYPALISHIRING", 4))
print(solution.convert("A", 1))
"""
~my first solution:
class Solution(object):
    def convert(self, s, numRows):
        """
"""": type s: str
: type numRows: int
: rtype: str"""
"""
        # her satır aslında kendisine denk gelecek harfleri saklayacak.
        if len(s) <= numRows or numRows == 1:
            return s
        store_lines = []
        # numrows+numrows-2 and nums< ise direkt gösterdiği büük eşit ise şuan bilmiyorum :D
        for i in range(numRows):
            store_lines.append([])
        index = numRows+numRows-2

        for letter_index in range(len(s)):
            if letter_index % index < numRows:
                store_lines[letter_index % index].append(s[letter_index])
                deneme_index = letter_index-1
            else:

                store_lines[deneme_index % index].append(s[letter_index])
                deneme_index = deneme_index-1

        zigzag = ""
        zig_zag = ""
        for i in store_lines:

            zigzag = "".join(i)

            zig_zag += zigzag
        return zig_zag

"""
