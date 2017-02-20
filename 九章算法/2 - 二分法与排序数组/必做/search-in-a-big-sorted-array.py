"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if not reader or not target:
            return -1
        
        index = 0
        while reader.get(index) < target:
            index = 2 * index + 1 
        
        left = 0
        right = index
        
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid
        
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right    
        return -1
        