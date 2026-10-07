class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x = -x
            i = 0
            rev = 0
            while i < x:
                dig = x%10
                rev = rev*10+dig
                x = x//10
            if rev < -2147483648 or rev > 2147483647:
                return 0
            return -rev
        else:
            i = 0
            rev = 0
            while i < x:
                dig = x%10
                rev = rev*10+dig
                x = x//10
            if rev < -2147483648 or rev > 2147483647:
               return 0
            return rev

        