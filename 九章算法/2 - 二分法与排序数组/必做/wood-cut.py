class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or not k:
            return 0
            
        left = 1
        right = max(L)
        
        while left + 1 < right:
            mid = (right - left) / 2 + left
            maxNum = self.checkWood(L, mid)
            if maxNum >= k:
                left = mid
            else:
                right = mid
        
        if self.checkWood(L, right) >= k:
            return right
        if self.checkWood(L, left) >= k:
            return left
        return 0
        
    def checkWood(self, L, length):
        result = 0
        for wood in L:
            result += wood / length
        return result