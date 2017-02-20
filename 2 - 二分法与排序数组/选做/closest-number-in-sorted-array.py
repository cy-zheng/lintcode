class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        # Write your code here
        if not A or target is None:
            return -1
            
        left = 0
        right = len(A) - 1
        
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if A[mid] >= target:
                right = mid
            else:
                left = mid
                
        if A[left] == target:
            return left
        elif A[right] == target:
            return right
        elif abs(A[left] - target) <= abs(A[right] - target):
            return left
        else:
            return right