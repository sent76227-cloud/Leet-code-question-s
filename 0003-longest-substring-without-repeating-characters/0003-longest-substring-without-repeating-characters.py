class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub= ""
        long = 0
        prev = 0
        for i in s:
          if i not in sub:
            sub= sub+i
          else:
            sub = sub[sub.index(i)+1:]
            sub = sub + i
          long = max(len(sub),long)  
        return long
        
        










        # char_map = {}
        # left = 0
        # max_length = 0
        # for right, char in enumerate(s):
        #     if char in char_map and char_map[char] >= left:
        #         left = char_map[char] + 1
        #     char_map[char] = right
        #     max_length = max(max_length, right - left + 1)
        # return max_length
       