public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int maxProduct(int[] nums) {
        // write your code here
        int result = Integer.MIN_VALUE;
        if (nums == null || nums.length == 0){
            return result;
        }
        long[] prefix = new long[nums.length + 1];
        prefix[0] = 1;
        int maxNegPrefix = 1;
        int minPosPrefix = 1;
        
        for (int i = 0; i < nums.length; i++){
            prefix[i + 1] = prefix[i] * nums[i];
            if (prefix[i + 1] > 0){
                result = (int)Math.max(result, prefix[i + 1] / minPosPrefix);
                minPosPrefix = (int)Math.min(minPosPrefix, prefix[i + 1]);
            }
            else if(prefix[i + 1] < 0){
                result = (int)Math.max(result, prefix[i + 1] / maxNegPrefix);
                maxNegPrefix = maxNegPrefix < 0 ? 
                    (int)Math.max(maxNegPrefix, prefix[i + 1]) : (int)prefix[i + 1];
            } 
            else{
                result = (int)Math.max(result, 0);
                prefix[i + 1] = 1;
                maxNegPrefix = 1;
                minPosPrefix = 1;
            }
        }
        return result;
    }
}