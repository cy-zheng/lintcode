class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if not A:
            return -1
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if A[mid] == target:
                left = mid
            elif A[mid] < target:
                left = mid
            else:
                right = mid
        if A[right] == target:
            return right
        if A[left] == target:
            return left
        return -1