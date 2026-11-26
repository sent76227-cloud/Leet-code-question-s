class Solution(object):
    def longestPalindrome(self, s):
        start, end = 0, 0

        for i in range(len(s)):
            for l, r in ((i, i), (i, i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1

                if r - l - 2 > end - start:
                    start, end = l + 1, r - 1

        return s[start:end+1]