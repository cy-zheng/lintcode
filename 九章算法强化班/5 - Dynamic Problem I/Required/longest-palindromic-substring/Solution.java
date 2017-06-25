public class Solution {
    /**
     * @param s input string
     * @return the longest palindromic substring
     */
    public String longestPalindrome(String s) {
        // Write your code here
        if (s == null || s.length() <= 1) return s;
        boolean[][] dp = new boolean[s.length()][s.length()];
        int start = 0;
        int end = 1;
        int maxLength = 1;
        
        for (int i = 0; i < s.length(); i++){
            dp[i][i] = true;
        }
        
        for (int i = 1; i < s.length(); i++){
            for (int j = 0; j < s.length(); j++){
                if (j + i >= s.length()){
                    break;
                }
                if (i == 1){
                    dp[j][j + i] = s.charAt(j) == s.charAt(j + i);
                }
                else{
                    dp[j][j + i] = dp[j + 1][j + i - 1] && s.charAt(j) == s.charAt(j + i);
                }
                if (dp[j][j + i] && i + 1 > maxLength){
                    maxLength = i + 1;
                    start = j;
                    end = j + i + 1;
                }
            }
        }
        return s.substring(start, end);
    }
}