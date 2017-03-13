class Solution:
    """
    @param {int} n a integer
    @return {int} a integer
    """
    def __init__(self):
        self.cache = {0: 1, 1: 1, 2: 2} 

    def climbStairs2(self, n):
        # Write your code here
        if n in self.cache:
            return self.cache[n]
        else:
            result = self.climbStairs2(n - 1) + self.climbStairs2(n - 2) \
                        + self.climbStairs2(n - 3)
            self.cache[n] = result
            return result