class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A or target is None:
            return [-1, -1]
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if A[mid] >= target:
                right = mid
            else:
                left = mid
        if A[left] == target:
            leftBound = left
        elif A[right] == target:
            leftBound = right
        else:
            return [-1, -1]
            
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if A[mid] > target:
                right = mid
            else:
                left = mid
        if A[right] == target:
            rightBound = right
        elif A[left] == target:
            rightBound = left
        
        return [leftBound, rightBound]
        
        