public class Solution {
    /**
     * @param n: an integer
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int n) {
        // write your code here
        if (n <= 0) return false;
        boolean[] dp = new boolean[2];
        dp[0] = true;
        dp[1] = true;
        if (n < 3) return dp[n - 1];
        for (int i = 3; i <= n; i++){
            dp[(i - 1) % 2] = (!dp[(i - 2) % 2]) || (!dp[(i - 3) % 2]);
        }
        return dp[(n -1) % 2];
    }
}