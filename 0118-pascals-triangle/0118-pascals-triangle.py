class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        matrix = []

        for i in range(1,numRows+1):
            new = []
            if i == 1:
                new.append(i)
            else:
                new.append(1)
                pre = matrix[-1]
                for i in range(1,len(pre)):
                    value = pre[i-1] + pre[i]
                    new.append(value)
                new.append(1)
            matrix.append(new)
        return matrix