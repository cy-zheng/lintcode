/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
import java.util.*; 

public class Solution {
    /**
     * @param A: Given an integer array with no duplicates.
     * @return: The root of max tree.
     */
    public TreeNode maxTree(int[] A) {
        // write your code here
        // http://www.cnblogs.com/lishiblog/p/4187936.html
        if (A == null || A.length == 0) return null;
        // stack is descending
        Stack<TreeNode> stack = new Stack<>();
        for (int i : A){
            TreeNode cur = new TreeNode(i);
            if (stack.size() == 0 || stack.peek().val > cur.val){
                stack.push(cur);
            }
            else {
                TreeNode old = stack.pop();
                TreeNode pre = null;
                while (stack.size() > 0 && stack.peek().val < cur.val){
                    pre = stack.pop();
                    pre.right = old;
                    old = pre;
                }
                cur.left = old;
                stack.push(cur);
            }
        }
        // finally merge
        TreeNode root = stack.pop();
        TreeNode pre = null;
        while (stack.size() > 0){
            pre = stack.pop();
            pre.right = root;
            root = pre;
        }
        return root;
    }
}