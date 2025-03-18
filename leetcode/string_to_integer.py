class Solution(object):
    def myAtoi(self, s):
        number = ""
        is_negative = False
        is_positive = False
        s = s.strip()
        for letter in s:

            # Sayı negatif mi kontrolünü yapar
            if letter == "-" and not len(number) and not is_negative:
                is_negative = True
                continue
            if letter == "+" and not len(number) and not is_positive:
                is_positive = True
                continue
            if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                number += letter
            else:
                break

        if is_negative and is_positive:
            return 0
        if not len(number):
            return 0
        number = int(number)
        if is_negative:
            number = -1*number
        if number < (-2)**31:
            return (-2)**31
        if number > (2**31)-1:
            return (2**31)-1
        return number


solution = Solution()
print(solution.myAtoi("42"))
print(solution.myAtoi("1337c0d3"))
print(solution.myAtoi("-042"))
print(solution.myAtoi("0-1"))
print(solution.myAtoi("words and 987"))
print(solution.myAtoi("+-12"))
print(solution.myAtoi("-91283472332"))
