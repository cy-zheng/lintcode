class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if not A or target is None:
            return -1
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if A[right] < target:
                if A[mid] < A[right]:
                    right = mid
                elif A[mid] > target:
                    right = mid
                else:
                    left = mid
            else:
                if A[mid] < target:
                    left = mid
                elif A[mid] > A[right]:
                    left = mid
                else:
                    right = mid
        
        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1
        
        
                