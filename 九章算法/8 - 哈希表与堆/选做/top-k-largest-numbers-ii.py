import heapq
import sys
class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.k = k
        self.heap = []

        
    # @param {int} num an integer
    def add(self, num):
        # Write your code here
        heapq.heappush(self.heap, sys.maxint - num)
        


    # @return {int[]} the top k largest numbers
    def topk(self):
        # Write your code here
        result = []
        for i in range(min(self.k, len(self.heap))):
            result.append(sys.maxint - heapq.heappop(self.heap))
            
        for i in result:
            heapq.heappush(self.heap, sys.maxint - i)
        return result
            

