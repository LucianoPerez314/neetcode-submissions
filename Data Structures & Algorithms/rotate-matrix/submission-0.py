class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (1, 0) -> (0, 1)
        # (0, 0) => (2, 0)
        n = len(matrix)
        # make matrix tranpose
        for i in range(n):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                
        print(matrix)
        # reverse each row.
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return
