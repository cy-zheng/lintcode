class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        if not pages or not k:
            return 0
            
        left = max(pages)
        right = sum(pages)
        
        while left + 1 < right:
            mid = (right - left) / 2 + left
            staffCount = self.copyHelper(pages, mid)
            if staffCount <= k:
                right = mid
            else:
                left = mid
        
        if self.copyHelper(pages, left) <= k:
            return left
        else:
            return right
            
    def copyHelper(self, pages, maxWork):
        result = 0
        temp = 0
        for page in pages:
            if temp + page <= maxWork:
                temp += page
            else:
                temp = page
                result += 1
        result += 1
        return result