class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        signs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                if stack[-1] == signs[i]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0        