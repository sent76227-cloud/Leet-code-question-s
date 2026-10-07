class Solution(object):
    def spiralOrder(self, matrix):
        
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # 1. Right →
            column = left
            while column <= right:
                result.append(matrix[top][column])
                column = column + 1

            top = top + 1

            # 2. Down ↓
            row = top
            while row <= bottom:
                result.append(matrix[row][right])
                row = row + 1

            right = right - 1

            # 3. Left ←
            if top <= bottom:
                column = right
                while column >= left:
                    result.append(matrix[bottom][column])
                    column = column - 1

                bottom = bottom - 1

            # 4. Up ↑
            if left <= right:
                row = bottom
                while row >= top:
                    result.append(matrix[row][left])
                    row = row - 1

                left = left + 1

        return result