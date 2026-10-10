class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_start = 0
        row_end = len(matrix)-1
        coloum_start = 0
        coloum_end = len(matrix[0])-1
        new = []
        for coloum in range(coloum_start,coloum_end+1):
           a = []
           for i in range(row_end,row_start-1,-1):
               a.append(matrix[i][coloum])
           new.append(a)
        
        
        matrix[:] = new
        return matrix
