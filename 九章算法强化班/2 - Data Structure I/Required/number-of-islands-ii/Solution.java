/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
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
     * @param n an integer
     * @param m an integer
     * @param operators an array of point
     * @return an integer array
     */
    private Pair find(Pair[][] map, int x, int y){
        if (map[x][y].x == x && map[x][y].y == y) return map[x][y];
        Pair result = find(map, map[x][y].x, map[x][y].y);
        map[x][y] = result;
        return result;
    }

    private boolean connect(Pair[][] map, int x1, int y1, int x2, int y2){
        Pair p1 = find(map, x1, y1);
        Pair p2 = find(map, x2, y2);
        if (p1.x != p2.x || p1.y != p2.y) {
            int tarX = p1.x;
            int tarY = p1.y;
            map[tarX][tarY].x = p2.x;
            map[tarX][tarY].y = p2.y;
            return true;
        }
        return false;
    }

    private boolean check(Pair[][] map, int x, int y){
        if (x < 0 || x >= map.length) return false;
        if (y < 0 || y >= map[0].length) return false;
        return map[x][y] != null;
    }

    public List<Integer> numIslands2(int n, int m, Point[] operators) {
        // Write your code here
        Pair[][] map = new Pair[n][m];
        List<Integer> result = new ArrayList<>();
        if (operators == null || operators.length == 0){
            return result;
        }
        int islandCount = 0;
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        for (Point p : operators){
            if (map[p.x][p.y] != null){
                result.add(islandCount);
                continue;
            }
            islandCount++;
            map[p.x][p.y] = new Pair(p.x, p.y);
            for (int i = 0; i < 4; i++){
                int x = p.x + dx[i];
                int y = p.y + dy[i];
                if (check(map, x, y)){
                    if(connect(map, x, y, p.x, p.y)) islandCount--;
                }
            }
            result.add(islandCount);
        }
        return result;
    }
}