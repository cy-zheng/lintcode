public class Solution {
    /**
     * @param values: an array of integers
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int[] values) {
        // write your code here
        if (values == null || values.length < 3)
            return true;

        int n = values.length;
        int[][] dp = new int[n][n];
        boolean[][] flag = new boolean[n][n];
        int sum = 0;
        for (int v : values)
            sum += v;
        boolean result = findResult(dp, flag, values, 0, n - 1) > sum / 2;
        return result;
    }

    private int findResult(int[][] dp, boolean[][] flag, int[] values, int start, int end) {
        if (flag[start][end])
            return dp[start][end];
        flag[start][end] = true;
        if (start == end)
            dp[start][end] = values[start];
        else if (start + 1 == end){
            dp[start][end] = Math.max(values[start], values[end]);
        }
        else{
            dp[start][end] = Math.max(
                    Math.min(
                            findResult(dp, flag, values, start + 2, end),
                            findResult(dp, flag, values, start + 1, end - 1)
                    ) + values[start],
                    Math.min(
                            findResult(dp, flag, values, start + 1, end - 1),
                            findResult(dp, flag, values, start, end - 2)
                    ) + values[end]
            );
        }
        return dp[start][end];
    }
}