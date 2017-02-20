class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Write your code here
        result = []
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if A[mid] >= target:
                right = mid
            else:
                left = mid
        
        while len(result) < k:
            if left >= 0 and right <= len(A) - 1:
                if abs(A[left] - target) <= abs(A[right] - target):
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1
            elif left >= 0:
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        return result