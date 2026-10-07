class Solution(object):
    def spiralOrder(self, matrix):
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Right →
            column = left
            while column <= right:
                result.append(matrix[top][column])
                column += 1
            top += 1

            # Down ↓
            row = top
            while row <= bottom:
                result.append(matrix[row][right])
                row += 1
            right -= 1

            # Left ←
            if top <= bottom:
                column = right
                while column >= left:
                    result.append(matrix[bottom][column])
                    column -= 1
                bottom -= 1

            # Up ↑
            if left <= right:
                row = bottom
                while row >= top:
                    result.append(matrix[row][left])
                    row -= 1
                left += 1

        return result