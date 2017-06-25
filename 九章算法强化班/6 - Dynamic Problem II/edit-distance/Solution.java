public class Solution {
    /**
     * @param word1 & word2: Two string.
     * @return: The minimum number of steps.
     */
    public int minDistance(String word1, String word2) {
        // write your code here
        if (word1 == word2) return 0;
        if (word1 == null || word1.length() == 0) return word2.length();
        if (word2 == null || word2.length() == 0) return word1.length();
        
        int[][] dp = new int[2][word2.length() + 1];
        
        for (int j = 1; j < word2.length() + 1; j++){
            dp[0][j] = j;
        }
        
        for (int i = 1; i < word1.length() + 1; i++){
            dp[i % 2][0] = i;
            for (int j = 0; j < word2.length(); j++){
                if (word1.charAt(i - 1) != word2.charAt(j)){
                    dp[i % 2][j + 1] = Math.min(
                            dp[(i - 1) % 2][j],
                            Math.min(dp[(i - 1) % 2][j + 1], dp[i % 2][j])
                        ) + 1;
                }
                else{
                    // why?
                    // dp[i % 2][j + 1] =  dp[(i - 1) % 2][j];
                    // left add, up add, left up replace(+0)
                    dp[i % 2][j + 1] =  Math.min(
                            dp[(i - 1) % 2][j],
                            Math.min(dp[(i - 1) % 2][j + 1] + 1, dp[i % 2][j] + 1)
                        ) ;
                }
            }
        }

        return dp[word1.length() % 2][word2.length()];
    }
}