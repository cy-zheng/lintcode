import java.util.*;
public class Solution {
    /**
     * @param S: A list of integers
     * @return: An integer
     */
    public int triangleCount(int S[]) {
        // write your code here
        Arrays.sort(S);
        int result = 0;
        for(int i = S.length - 1; i > 1; i--){
            result += twoSum(S, 0, i - 1, S[i]);
        }
        return result;
    }
    
    private int twoSum(int S[], int start, int end, int target){
        int result = 0;
        while (start < end){
            if (S[start] + S[end] > target){
                result += end - start;
                end--;
            }
            else{
                start++;
            }
        }
        return result;
    }
}
