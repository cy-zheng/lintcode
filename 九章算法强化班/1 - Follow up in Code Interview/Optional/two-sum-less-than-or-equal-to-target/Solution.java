import java.util.*;
public class Solution {
    /**
     * @param nums an array of integer
     * @param target an integer
     * @return an integer
     */
    public int twoSum5(int[] nums, int target) {
        // Write your code here
        int result = 0;
        if (nums == null || nums.length < 2){
            return result;
        }
        Arrays.sort(nums);
        int left = 0;
        int right = nums.length - 1;
        while (left < right){
            if (nums[left] + nums[right] <= target){
                result += right - left;
                left++;
            }
            else{
                right--;
            }
        }
        return result;
    }
}