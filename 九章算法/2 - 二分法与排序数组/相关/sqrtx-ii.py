class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):
        # Write your code here
        if not x:
            return 0
        left = 0.0
        right = x if x > 1 else 1
        while left + 1e-12 < right:
            mid = (right - left) / 2 + left
            if mid ** 2 <= x - 1e-12:
                left = mid
            elif mid ** 2 >= x + 1e-12:
                right = mid
            else:
                right = mid
                break
        if right ** 2 <= x:
            return right
        if left ** 2 <= x:
            return left
        return 0