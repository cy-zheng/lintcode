class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        if not A or target is None:
            return False
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if A[right] < target:
                if A[mid] < A[right]:
                    right = mid
                elif A[mid] == A[right]:
                    if self.judge(A, left, mid, right):
                        left = mid
                    else:
                        right = mid
                elif A[mid] > target:
                    right = mid
                else:
                    left = mid
            else:
                if A[mid] < target:
                    left = mid
                elif A[mid] > A[right]:
                    left = mid
                elif A[mid] == A[right]:
                    if self.judge(A, left, mid, right):
                        left = mid
                    else:
                        right = mid
                else:
                    right = mid
        
        if A[left] == target:
            return True
        if A[right] == target:
            return True
        return False
        
    def judge(self, A, left, mid, right):
        temp = None
        for i in A[left:mid + 1]:
            if temp is None or i == temp:
                temp = i
            else:
                return False
        return True
        