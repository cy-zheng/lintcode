class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        result = 0
        if not matrix or target is None:
            return result
        row = len(matrix) - 1
        col = 0
        while col <= len(matrix[0]) - 1 and row >= 0:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                result += 1
                col += 1
                row -= 1
        return result