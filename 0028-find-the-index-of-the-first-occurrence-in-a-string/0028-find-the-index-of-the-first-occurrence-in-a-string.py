class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        x= 0
        for i in range(len(haystack) - len(needle) + 1):
            check = ""
            for j in range(0,len(needle)):
                if haystack[i+j] == needle[j]:
                     check = check+needle[j]
            if check == needle:
                x = 1
                return i
                break
        if x == 0:
          return -1
                    


        