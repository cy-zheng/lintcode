public class Solution {
    /**
     * @param A an array of Integer
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequence(int[] A) {
        // Write your code here
        int result = 0;
        if (A == null || A.length == 0) return result;
        int[] dp = new int[A.length];
        for (int i = 0; i < A.length; i++){
            if (i == 0) {
                dp[i] = 1;
            }
            else{
                if (A[i] > A[i - 1]){
                    dp[i] = dp[i - 1] + 1;
                }
                else{
                    dp[i] = 1;
                }
            }
            result = Math.max(result, dp[i]);
        }
        for (int i = A.length - 1; i >= 0; i--){
            if (i == A.length - 1) {
                dp[i] = 1;
                continue;
            }
            else{
                if (A[i] > A[i + 1]){
                    dp[i] = dp[i + 1] + 1;
                }
                else{
                    dp[i] = 1;
                }
            }
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}