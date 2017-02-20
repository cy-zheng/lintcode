class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        if not A or not target:
            return 0
            
        left1 = 0
        right1 = len(A) - 1
        while left1 + 1 < right1:
            mid1 = (right1 - left1) / 2 + left1
            if A[mid1] >= target:
                right1 = mid1
            else:
                left1 = mid1
        
        startIndex = -1
        if A[left1] == target:
            startIndex = left1
        elif A[right1] == target:
            startIndex = right1
        if startIndex == -1:
            return 0
        
        left2 = 0
        right2 = len(A) - 1
        while left2 + 1 < right2:
            mid2 = (right2 - left2) / 2 + left2
            if A[mid2] <= target:
                left2 = mid2
            else:
                right2 = mid2
        
        endIndex = -1
        if A[right2] == target:
            endIndex = right2
        elif A[left2] == target:
            endIndex = left2
        if endIndex == -1:
            return 0

        return endIndex - startIndex + 1
        