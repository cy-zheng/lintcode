/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */
import java.util.*;

class Point implements Comparable<Point>{
    public int x;
    public int isTakeOff;

    public Point(int x, int flag){
        this.x = x;
        this.isTakeOff = flag;
    }

    public int compareTo(Point p){
        if (this.x == p.x){
            return this.isTakeOff - p.isTakeOff;
        }
        return this.x - p.x;
    }
}

class Solution {
    /**
     * @param intervals: An interval array
     * @return: Count of airplanes are in the sky.
     */
    public int countOfAirplanes(List<Interval> airplanes) {
        // write your code here
        int result = 0;
        int cur = 0;
        if (airplanes == null || airplanes.size() == 0) return result;
        List<Point> points = new ArrayList<>();
        for (Interval i : airplanes){
            points.add(new Point(i.start, 1));
            points.add(new Point(i.end, 0));
        }
        Collections.sort(points);

        for (Point p : points){
            if (p.isTakeOff == 1){
                cur++;
            }
            else{
                cur--;
            }
            result = Math.max(result, cur);
        }
        return result;
    }
}