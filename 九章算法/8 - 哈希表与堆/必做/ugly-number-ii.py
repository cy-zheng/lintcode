import heapq

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        visited = set([])
        value_list = [2, 3, 5]
        for i in range(1, n):
            num = heapq.heappop(heap)
            for v in value_list:
                if num * v not in visited:
                    visited.add(num * v)
                    heapq.heappush(heap, num * v)
        return heapq.heappop(heap)

