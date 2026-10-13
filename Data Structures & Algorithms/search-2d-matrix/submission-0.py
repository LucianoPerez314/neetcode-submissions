class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start, end = 0, m * n - 1
        mid = (end + start) // 2
        while start <= end:
            i = (mid // n)
            j = (mid % n)
            if target == matrix[i][j]:
                return True
            if target < matrix[i][j]:
                end = mid - 1
            elif target > matrix[i][j]:
                start = mid + 1
            mid = (end + start) // 2
        return False
        # 5, (1, 1)