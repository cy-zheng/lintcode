public class Solution {
    /**
     * @param A an integer array
     * @return an integer
     */
    public int stoneGame(int[] A) {
        // Write your code here
        if (A == null || A.length == 0) return 0;
        int n = A.length;
        int[][] dp = new int[n][n];
        boolean[][] flag = new boolean[n][n];
        int[] prefix = new int[n + 1];

        for (int i = 0; i < A.length; i++){
            prefix[i + 1] = prefix[i] + A[i];
            flag[i][i] = true;
        }

        return getCost(dp, flag, prefix, A, 0, A.length - 1);
    }

    private int getCost(int[][] dp, boolean[][] flag, int[] prefix,
                        int[] A, int start, int end){
        if(flag[start][end]) return dp[start][end];
        int result = Integer.MAX_VALUE;
        for (int i = start; i < end; i++){
            result = Math.min(result,
                    getCost(dp, flag, prefix, A, start, i) +
                            getCost(dp, flag, prefix, A, i + 1, end));
        }
        dp[start][end] = result + prefix[end + 1] - prefix[start];
        flag[start][end] = true;
        return dp[start][end];
    }
}