class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def __init__(self):
        self.cache = {0: 1, 1: 1} 
    def climbStairs(self, n):
        # write your code here
        if n in self.cache:
            return self.cache[n]
        else:
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.cache[n] = result
            return result
