class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if len(A) <= 1:  
            return True  
        zero_index = []  
        for i in range(len(A))[:-1]:  
            if A[i] == 0:  
                zero_index.append(i)  
        for zindex in zero_index[::-1]:  
            flag = False  
            for tindex in range(0,zindex)[::-1]:  
                if (A[tindex] + tindex) > zindex:  
                    flag = True  
                    break  
            if not flag:  
                return flag  
        return True  