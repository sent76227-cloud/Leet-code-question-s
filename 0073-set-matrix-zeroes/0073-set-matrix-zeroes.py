class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        rows = []
        cols = []

        # Step 1: Find original zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        # Step 2: Make those rows zero
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        # Step 3: Make those columns zero
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0
