import java.util.*;

class TrieNode {
    String s;
    boolean isString;
    HashMap<Character, TrieNode> subtree;
    public TrieNode() {
        isString = false;
        subtree = new HashMap<Character, TrieNode>();
        s = "";
    }
}

class TrieTree{
    TrieNode root ;
    public TrieTree(TrieNode TrieNode) {
        root = TrieNode;
    }
    public void insert(String s) {
        TrieNode now = root;
        for (int i = 0; i < s.length(); i++) {
            if (!now.subtree.containsKey(s.charAt(i))) {
                now.subtree.put(s.charAt(i), new TrieNode());
            }
            now  =  now.subtree.get(s.charAt(i));
        }
        now.s = s;
        now.isString  = true;
    }
    public boolean find(String s){
        TrieNode now = root;
        for (int i = 0; i < s.length(); i++) {
            if (!now.subtree.containsKey(s.charAt(i))) {
                return false;
            }
            now  =  now.subtree.get(s.charAt(i));
        }
        return now.isString;
    }
    public boolean startsWith(String s){
        TrieNode now = root;
        for (int i = 0; i < s.length(); i++) {
            if (!now.subtree.containsKey(s.charAt(i))) {
                return false;
            }
            now  =  now.subtree.get(s.charAt(i));
        }
        return true;
    }
}

public class Solution {
    /**
     * @param board: A list of lists of character
     * @param words: A list of string
     * @return: A list of string
     */
    public ArrayList<String> wordSearchII(char[][] board, ArrayList<String> words) {
        // write your code here
        ArrayList<String> result = new ArrayList<>();
        Set<String> set = new HashSet<>();
        if (words == null || words.size() == 0) return result;
        TrieTree tree = new TrieTree(new TrieNode());
        for (String s : words){
            tree.insert(s);
        }
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                visited[i][j] = false;
            }
        }
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                visited[i][j] = true;
                dfs(board, visited, set, Character.toString(board[i][j]), tree, i, j);
                visited[i][j] = false;
            }
        }
        for (Object s : set.toArray()){
            result.add((String) s);
        }
        return result;
    }

    private void dfs(char[][] board, boolean[][] visited,
                     Set<String> result, String sub, TrieTree tree, int i, int j){
        if (!tree.startsWith(sub)) return;
        if (tree.find(sub)) result.add(sub);
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        for (int k = 0; k < 4; k++){
            int x = i + dx[k];
            int y = j + dy[k];
            if (check(visited, x, y)){
                visited[x][y] = true;
                dfs(board, visited, result, sub + Character.toString(board[x][y]), tree, x, y);
                visited[x][y] = false;
            }
        }
    }

    private boolean check(boolean[][] visited, int i, int j){
        if (i < 0 || i >= visited.length) return false;
        if (j < 0 || j >= visited[0].length) return false;
        return !visited[i][j];
    }
}