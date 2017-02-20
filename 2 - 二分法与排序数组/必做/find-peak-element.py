class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if not A:
            return -1
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if mid - 1 < 0:
                left = mid
            elif mid + 1 >= len(A):
                right = mid
            elif A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
                left = mid
            elif A[mid - 1] > A[mid] and A[mid] > A[mid + 1]:
                right = mid
            elif A[mid - 1] > A[mid] and A[mid] < A[mid + 1]:
                left = mid
            elif A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
                
        if right - 1 >= 0 and right + 1 < len(A) \
            and A[right - 1] < A[right] and A[right] > A[right + 1]:
            return right
        else:
            return left