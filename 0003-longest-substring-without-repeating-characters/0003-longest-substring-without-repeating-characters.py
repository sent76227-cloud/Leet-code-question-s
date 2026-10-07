class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        new = ""
        max = 0 
        for i in s:
            if i not in new:
                new = new + i
            else:
                new = new[new.index(i)+1::]
                new = new + i
            if len(new) > max:
                max = len(new)

        return max 
        












        # char_map = {}
        # left = 0
        # max_length = 0
        # for right, char in enumerate(s):
        #     if char in char_map and char_map[char] >= left:
        #         left = char_map[char] + 1
        #     char_map[char] = right
        #     max_length = max(max_length, right - left + 1)
        # return max_length
       