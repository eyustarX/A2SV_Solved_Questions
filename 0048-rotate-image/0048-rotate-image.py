class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = [[1001]*len(matrix) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                k = len(matrix) - 1 -i
                mat[j][k] = matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = mat[i][j]
        
        

    