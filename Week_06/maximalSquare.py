class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        columns = len(matrix[0])
        if rows == 0 or columns == 0:
            return 0
        max_side = 0
        auxiliary = [[0] * columns for _ in range(rows)]
        for index1 in range(rows):
            for index2 in range(columns):
                if matrix[index1][index2] == '1':
                    if index1 == 0 or index2 == 0:
                        auxiliary[index1][index2] = 1
                    else:
                        auxiliary[index1][index2] = min(auxiliary[index1 - 1][index2 - 1], auxiliary[index1][index2 - 1], auxiliary[index1 - 1][index2]) + 1
                    max_side = max(max_side, auxiliary[index1][index2])
        result = max_side ** 2
        return result
