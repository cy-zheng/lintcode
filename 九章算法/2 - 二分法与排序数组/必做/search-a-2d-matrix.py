class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if n == 0:
            return False
        left, right = 0, m - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if matrix[mid][0] < target:
                left = mid
            elif matrix[mid][0] > target:
                right = mid
            else:
                return True
                
        if matrix[right][0] <= target:
            row_num = right
        elif matrix[left][0] <= target:
            row_num = left
        elif left - 1 >= 0 and matrix[left][0] <= target:
            row_num = left - 1
        else:
            return False
            
        left, right = 0, n - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if matrix[row_num][mid] < target:
                left = mid
            elif matrix[row_num][mid] > target:
                right = mid
            else:
                return True
        if matrix[row_num][left] == target or matrix[row_num][right] == target:
            return True
        return False