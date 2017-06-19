public class Solution {
    /**
     * @param A: An array of non-negative integers.
     * return: The maximum amount of money you can rob tonight
     */
    public long houseRobber(int[] A) {
        // write your code here
        if (A == null || A.length == 0) return 0;
        // integer overflow
        long[] dp = new long[2];
        dp[1] = 0;
        dp[0] = A[0];

        for (int i = 1; i < A.length; i++){
            dp[i % 2] = Math.max(dp[i % 2] + A[i], dp[(i + 1) % 2]);
        }
        return Math.max(dp[0], dp[1]);
    }
}