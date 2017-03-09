class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        m, n = len(image), len(image[0])
        left, right = 0, x
        while left + 1 < right:
            mid = (right - left) / 2 + left
            flag = False
            for i in range(n):
                if image[mid][i] == '1':
                    flag = True
                    break
            if not flag:
                left = mid
            else:
                right = mid
        flag = False
        for i in range(n):
            if image[left][i] == '1':
                flag = True
                break
        if not flag:
            row1 = right
        else:
            row1 = left
            
        left, right = x, m - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            flag = False
            for i in range(n):
                if image[mid][i] == '1':
                    flag = True
                    break
            if not flag:
                right = mid
            else:
                left = mid
        flag = False
        for i in range(n):
            if image[right][i] == '1':
                flag = True
                break
        if not flag:
            row2 = left
        else:
            row2 = right  

        left, right = 0, y
        while left + 1 < right:
            mid = (right - left) / 2 + left
            flag = False
            for i in range(m):
                if image[i][mid] == '1':
                    flag = True
                    break
            
            if flag:
                right = mid
            else:
                left = mid
        flag = False
        for i in range(m):
            if image[i][left] == '1':
                flag = True
                break
        if not flag:
            col1 = right
        else:
            col1 = left
            
        left, right = y, n - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            flag = False
            for i in range(m):
                if image[i][mid] == '1':
                    flag = True
                    break
            if flag:
                left = mid
            else:
                right = mid
        flag = False
        for i in range(m):
            if image[i][right] == '1':
                flag = True
                break
        if not flag:
            col2 = left
        else:
            col2 = right
        return (row2 + 1 - row1) * (col2 + 1 - col1)
        