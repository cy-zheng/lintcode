class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        cache = [[None for i in range(n)] for j in range(n)]
        for j in range(n):
            cache[n - 1][j] = triangle[n - 1][j]
        for i in range(n - 1)[::-1]:
            for j in range(i + 1):
                cache[i][j] = min(cache[i + 1][j], cache[i + 1][j + 1]) + triangle[i][j]
        return cache[0][0]