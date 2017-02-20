class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if not x:
            return 0
        left = 1
        right = x
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if mid ** 2 <= x:
                left = mid
            else:
                right = mid
        if right ** 2 <= x:
            return right
        if left ** 2 <= x:
            return left
        return 0
                
        