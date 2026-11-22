class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        total = ""
        for i in range(1,len(s)//2+1):
          sub =  s[:i]
        
          if len(s)%i==0:
            total = ""
            for j in range(len(s)//i):
              total = total + sub
            if total == s:
                return True
        else:
           return False