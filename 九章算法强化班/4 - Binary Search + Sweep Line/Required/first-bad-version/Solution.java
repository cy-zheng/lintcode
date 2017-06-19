/**
 * public class SVNRepo {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use SVNRepo.isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/
class Solution {
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    public int findFirstBadVersion(int n) {
        // write your code here
        int left = 1;
        int right = n;
        while (left + 1 < right){
            int mid = (right - left) / 2 + left;
            if (SVNRepo.isBadVersion(mid)) right = mid;
            else left = mid;
        }
        if (SVNRepo.isBadVersion(left)) return left;
        return right;
    }
}
