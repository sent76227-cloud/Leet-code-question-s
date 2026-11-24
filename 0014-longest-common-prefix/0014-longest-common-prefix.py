class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        sub = ""
        for i in range(len(first)):
          if i < len(last) and first[i] == last[i]:
            sub = sub+first[i]
          else:
            break
        
        return sub