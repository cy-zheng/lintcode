import sys
from collections import deque
class Solution:
    # @param {int[]} nums an array of integers
    # @param {int} k1 an integer
    # @param {int} k2 an integer
    # @return {int} the largest sum
    def maxSubarray5(self, nums, k1, k2):
        # Write your code here
        ''' 
            This is an good idea to maintain a deque while finding the min 
            value of a list, and the list could add item and remove item.
            
            Heap can't delete any item easily, so we don't use heap.
        '''
        if len(nums) < k1:
            return 0
        queue = deque()
        prefix = [0]
        result = -sys.maxint - 1
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
            if queue and queue[0] < i - k2 + 1:
                queue.popleft()
            if i < k1 - 1:
                pass
            else:
                while queue and prefix[queue[-1]] > prefix[i - k1 + 1]:
                    queue.pop()
                queue.append(i - k1 + 1)
                result = max(result, prefix[-1] - prefix[queue[0]])
                
        return result
                