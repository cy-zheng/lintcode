public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    public int maxSubArray(int[] nums) {
        // write your code
        int result = Integer.MIN_VALUE;
        if (nums == null || nums.length == 0){
            return result;
        }
        int[] prefix = new int[nums.length + 1];
        int minPrefix = 0;
        for (int i = 0; i < nums.length; i++){
            prefix[i + 1] = prefix[i] + nums[i];
            result = Math.max(prefix[i + 1] - minPrefix, result);
            minPrefix = Math.min(minPrefix, prefix[i + 1]);
        }
        return result;
    }
}