public class Solution {
    /**
     * @param matrix a matrix of 0 and 1
     * @return an integer
     */
    public int maxSquare2(int[][] matrix) {
        // write your code here
        int n = matrix.length;
        if (n == 0)
            return 0;

        int m = matrix[0].length;
        if (m == 0)
            return 0;
        int result = 0;
        int[][] f = new int[n + 1][m + 1];
        int[][] u = new int[n + 1][m + 1];
        int[][] l = new int[n + 1][m + 1];

        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                if (matrix[i][j] == 0){
                    u[i + 1][j + 1] = u[i][j + 1] + 1;
                    l[i + 1][j + 1] = l[i + 1][j] + 1;
                }
                else {
                    f[i + 1][j + 1] = Math.min(f[i][j], Math.min(u[i][j + 1], l[i + 1][j])) + 1;
                    result = Math.max(result, f[i + 1][j + 1]);
                }
            }
        }
        return result * result;
    }
}