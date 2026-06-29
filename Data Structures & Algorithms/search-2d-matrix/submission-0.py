class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while r - l >= 0:
            mid = (l+r) // 2
            row, col = mid // n, mid % n
            guess = matrix[row][col]
            
            if guess == target:
                return True
            elif guess < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False