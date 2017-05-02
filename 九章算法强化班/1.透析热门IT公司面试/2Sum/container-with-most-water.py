class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        result = 0
        if not heights:
            return result
        
        left, right = 0, len(heights) - 1
        while left < right:
            result = max(result, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return result

        