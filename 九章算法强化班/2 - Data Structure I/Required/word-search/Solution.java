public class Solution {
    /**
     * @param board: A list of lists of character
     * @param word: A string
     * @return: A boolean
     */
    public boolean exist(char[][] board, String word) {
        // write your code here
        if (word == null || word.equals("")) return true;
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                visited[i][j] = true;
                if (dfs(board, visited, i, j, word)) return true;
                visited[i][j] = false;
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, boolean[][] visited, int i, int j, String word){
        if (word.equals("")) return true;
        if (board[i][j] != word.charAt(0)) return false;
        if (word.substring(1).equals("")) return true;
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        for (int k = 0; k < 4; k++){
            int x = i + dx[k];
            int y = j + dy[k];
            if (check(visited, x, y)){
                visited[x][y] = true;
                boolean result = dfs(board, visited, x, y, word.substring(1));
                visited[x][y] = false;
                if (result) return true;
            }
        }
        return false;
    }
    
    private boolean check(boolean[][] visited, int i, int j){
        if (i < 0 || i >= visited.length) return false;
        if (j < 0 || j >= visited[0].length) return false;
        return !visited[i][j];
    }
}