public class Solution {
    /**
     * @param nums: an array of integers
     * @param s: an integer
     * @return: an integer representing the minimum size of subarray
     */
    public int minimumSize(int[] nums, int s) {
        // write your code here
        if (nums == null || nums.length == 0) return -1;
        int result = -1;
        int j = 0;
        int sum = 0;
        for (int i = 0; i < nums.length; i++){
            boolean flag = false;
            if (i > 0){
                sum -= nums[i - 1];
                flag = true;
            }
            while (j < nums.length){
                if (!flag) {
                    sum += nums[j];
                }
                else {
                    flag = false;
                }
                if (sum >= s){
                    if (result == -1 || j - i + 1 < result){
                        result = j - i + 1;
                    }
                    break;
                }
                j++;
            }
        }
        return result;
    }
}