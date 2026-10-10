class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        matrix = []

        for i in range(rowIndex+1):
            new = []
            if i == 0:
                new.append(1)
            else:
                pre = matrix[-1]
                new.append(1)

                for j in range(1,len(pre)):
                    val = pre[j-1] + pre[j]
                    new.append(val)
                new.append(1)
            matrix.append(new)
        return matrix[rowIndex]