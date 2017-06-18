public class Solution {
    /** 
     *@param L: Given n pieces of wood with length L[i]
     *@param k: An integer
     *return: The maximum length of the small pieces.
     */
    public int woodCut(int[] L, int k) {
        // write your code here
        if (L == null || L.length == 0) return 0;
        int left = 1;
        int right = Integer.MIN_VALUE;
        for (int l : L){
            right = Math.max(right, l);
        }
        
        while (left + 1 < right){
            int mid = (right - left) / 2 + left;
            if (check(L, k, mid)){
                left = mid;
            }
            else{
                right = mid;
            }
        }
        
        if (check(L, k, right)) return right;
        if (check(L, k, left)) return left;
        return 0;
    }
    
    private boolean check(int[] L, int k, int mid){
        int result = 0;
        for (int l : L){
            result += l / mid;
        }
        return result >= k;
    }
}