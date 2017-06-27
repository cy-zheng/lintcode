public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        // write your code here
        if (m == 0 || A == null || A.length == 0) return 0;
        int n = A.length;
        boolean[][] dp = new boolean[n + 1][m + 1];
        dp[0][0] = true;
        for (int i = 1; i <= n; i++){
            for (int j = 0; j <= m; j++){
                dp[i][j] = dp[i - 1][j];
                if (A[i - 1] <= j){
                    dp[i][j] = dp[i][j] || dp[i - 1][j - A[i - 1]];
                }
            }
        }

        for (int i = m; i >= 0; i--){
            if (dp[n][i]){
                return i;
            }
        }
        return 0;
    }
}