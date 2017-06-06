class Solution {
    /*
     * @param k : description of k
     * @param nums : array of nums
     * @return: description of return
     */
    public int kthLargestElement(int k, int[] nums) {
        // write your code here
        return quickSelect(nums, 0, nums.length - 1, k);
    }

    private int quickSelect(int[] nums, int start, int end, int k){
        if (start >= end){
            return nums[start];
        }
        int pivot = nums[(start + end) / 2];
        int i = start;
        int j = end;
        while (i <= j){
            while (i <= j && nums[i] > pivot){
                i++;
            }
            while (i <= j && nums[j] < pivot){
                j--;
            }
            if (i <= j){
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                i++;
                j--;
            }
        }
        if(j - start >= k - 1){
            return quickSelect(nums, start, j, k);
        }
        else if(i - start <= k - 1){
            return quickSelect(nums, i, end, k - i + start);
        }
        else{
            return nums[j + 1];
        }
    }
};