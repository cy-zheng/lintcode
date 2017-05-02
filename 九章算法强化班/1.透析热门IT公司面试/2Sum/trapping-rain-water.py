class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        # http://blog.csdn.net/linhuanmars/article/details/20888505
        result = 0
        if not heights:
            return result
            
        left = [0] * len(heights)
        right = [0] * len(heights)
        max_value = 0
        for i in xrange(len(heights)):
            left[i] = max_value
            max_value = max(heights[i], max_value)
        max_value = 0
        for i in xrange(len(heights) - 1, -1, -1):
            right[i] = max_value
            max_value = max(heights[i], max_value) 

        for i in xrange(len(heights)):
            if min(left[i], right[i]) - heights[i] > 0:
                result += (min(left[i], right[i]) - heights[i])
        return result
        
            
