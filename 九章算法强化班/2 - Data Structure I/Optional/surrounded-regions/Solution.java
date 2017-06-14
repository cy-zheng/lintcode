import java.util.*;

class Pair{
    public int x, y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Solution {
    /**
     * @param board a 2D board containing 'X' and 'O'
     * @return void
     */
    public void surroundedRegions(char[][] board) {
        // Write your code here
        if (board == null || board.length == 0 || board[0].length == 0) return;
        Queue<Pair> queue = new LinkedList<>();
        boolean[][] visited = new boolean[board.length][board[0].length];
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        // bfs
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                if (visited[i][j] || board[i][j] == 'X') continue;
                visited[i][j] = true;
                queue.add(new Pair(i, j));
                List<Pair> tmp = new ArrayList<Pair>();
                boolean isBound = false;
                while(queue.size() > 0){
                    Pair node = queue.poll();
                    tmp.add(node);
                    for (int k = 0; k < 4; k++){
                        int x = node.x + dx[k];
                        int y = node.y + dy[k];
                        // 绝对不要在中途停止bfs的循环，否则就进入了一个大坑
                        if (checkBoundary(board, x, y)){
                            isBound = true;
                            continue;
                        }
                        if (board[x][y] == 'O' && !visited[x][y]){
                            queue.add(new Pair(x, y));
                            visited[x][y] = true;
                        }
                    }
                }
                if (!isBound){
                    for (Pair p : tmp){
                        board[p.x][p.y] = 'X';
                    }
                }

            }
        }
    }

    private boolean checkBoundary(char[][] board, int x, int y){
        if (x < 0 || x >= board.length) return true;
        if (y < 0 || y >= board[0].length) return true;
        return false;
    }
}