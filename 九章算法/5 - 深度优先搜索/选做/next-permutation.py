class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        for i in range(len(num))[::-1]:
            if i == 0:
                return num[::-1]
            else:
                if num[i] > num[i - 1]:
                    larger_index = None
                    for j in range(i, len(num))[::-1]:
                        if num[j] > num[i - 1]:
                            larger_index = j
                            break
                    num[i - 1], num[larger_index] = num[larger_index], num[i - 1] 
                    self.reverse(num, i)
                    return num
                    
    def reverse(self, num, i):
        j = len(num) - 1
        while i < j:
            num[i], num[j] = num[j], num[i]
            i += 1
            j -= 1
    