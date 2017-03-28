class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        n_set = set([])
        for n in nums:
            n_set.add(n)
            
        length = 0    
        for n in nums:
            up = down = n
            while up in n_set:
                up += 1
            while down in n_set:
                down -= 1
                
            length = max(length, up - down - 1)
            if length > len(nums) / 2:
                return length
            
        return length
            
            