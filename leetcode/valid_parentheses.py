class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_bracket = ("(", "[", "{")
        close_bracket = (")", "]", "}")
        open_list = []

        for x in s:
            if x in open_bracket:
                open_list.append(x)
            elif x in close_bracket:
                if not len(open_list) > 0:
                    return False
                if x == ")" and open_list[len(open_list)-1] == "(":
                    open_list.pop()
                elif x == "]" and open_list[len(open_list)-1] == "[":
                    open_list.pop()
                elif x == "}" and open_list[len(open_list)-1] == "{":
                    open_list.pop()
                else:
                    return False
        if len(open_list) > 0:
            return False
        return True


solution = Solution()
print(solution.isValid("}"))
