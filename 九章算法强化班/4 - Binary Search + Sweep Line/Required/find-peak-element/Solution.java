class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        // write your code here
        if (A == null || A.length == 0) return -1;
        int left = 0;
        int right = A.length - 1;
        
        while (left + 1 < right){
            int mid = (right - left) / 2 + left;
            if (mid != 0 && mid != A.length - 1){
                if (A[mid - 1] < A[mid] && A[mid] < A[mid + 1]){
                    left = mid;
                }
                else if (A[mid - 1] > A[mid] && A[mid] > A[mid + 1]){
                    right = mid;
                }
                else if (A[mid - 1] > A[mid] && A[mid] < A[mid + 1]){
                    right = mid;
                }
                else{
                    return mid;
                }
            }
        }
        if (A[left - 1] < A[left] && A[left] > A[left + 1]){
            return left;
        }
        return right;
    }
}
