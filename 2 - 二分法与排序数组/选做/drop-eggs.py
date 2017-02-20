class Solution:
    # @param {int} n an integer
    # @return {int} an integer
    def dropEggs(self, n):
        # Write your code here
        if not n:
            return 0
            
        left = 1
        right = n
        
        while left + 1 < right:
            mid = (right - left) / 2 + left
            temp = 0.5 * mid ** 2 + 0.5 * mid - n + 1
            if temp >= 0:
                right = mid
            elif temp < 0:
                left = mid
                
        return left if (0.5 * left ** 2 + 0.5 * left - n + 1) > 0 else right