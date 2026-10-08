class Solution(object):
    def spiralOrder(self, matrix):

        result = []

        row_start = 0
        row_end = len(matrix) - 1

        coloum_start = 0
        coloum_end = len(matrix[0]) - 1

        while row_start <= row_end and coloum_start <= coloum_end:

            # RIGHT →
            for i in range(coloum_start, coloum_end + 1):
                result.append(matrix[row_start][i])

            row_start = row_start + 1

            # DOWN ↓
            if row_start <= row_end:
                for i in range(row_start, row_end + 1):
                    result.append(matrix[i][coloum_end])

            coloum_end = coloum_end - 1

            # LEFT ←
            if coloum_start <= coloum_end and row_start <= row_end:
                for i in range(coloum_end, coloum_start - 1, -1):
                    result.append(matrix[row_end][i])

            row_end = row_end - 1

            # UP ↑
            if row_start <= row_end and coloum_start <= coloum_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][coloum_start])

            coloum_start = coloum_start + 1

        return result