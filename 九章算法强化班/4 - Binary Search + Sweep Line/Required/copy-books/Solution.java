public class Solution {
    /**
     * @param pages: an array of integers
     * @param k: an integer
     * @return: an integer
     */
    public int copyBooks(int[] pages, int k) {
        // write your code here
        if (pages == null || pages.length == 0) return 0;
        int left = Integer.MIN_VALUE;
        int right = 0;
        for (int i : pages){
            left = Math.max(left, i);
            right += i;
        }
        
        while (left + 1 < right){
            int mid = (right - left) / 2 + left;
            if (check(pages, k, mid)){
                right = mid;
            }
            else{
                left = mid;
            }
        }
        
        if (check(pages, k, left)) return left;
        return right;
    }
    
    private boolean check(int[] pages, int k, int mid){
        int cnt = 1;
        int work = 0;
        for (int p : pages){
            if (p > mid) return false;
            if (work + p > mid){
                cnt++;
                work = 0;
            }
            work += p;
        }
        return cnt <= k;
    }
}