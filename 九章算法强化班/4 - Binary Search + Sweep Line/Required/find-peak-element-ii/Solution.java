import java.util.*;

class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> findPeakII(int[][] A) {
        // write your code here
        if (A == null || A.length == 0 || A[0].length == 0) return null;
        boolean flag = true;
        int rowLeft = 0;
        int rowRight = A.length - 1;
        int colLeft = 0;
        int colRight = A[0].length - 1;
        List<Integer> r = new ArrayList<>();

        while (rowLeft + 1 < rowRight || colLeft + 1 < colRight){
            if (flag && rowLeft + 1 < rowRight){
                int mid = (rowRight - rowLeft) / 2 + rowLeft;
                int tmp = Integer.MIN_VALUE;
                int index = -1;
                for (int i = colLeft; i <= colRight; i++){
                    if (tmp < A[mid][i]){
                        tmp = A[mid][i];
                        index = i;
                    }
                }
                if (A[mid - 1][index] > A[mid][index]){
                    rowRight = mid;
                }
                else if (A[mid + 1][index] > A[mid][index]){
                    rowLeft = mid;
                }
                else{
                    r.add(mid);
                    r.add(index);
                    return r;
                }
            }
            else if (!flag && colLeft + 1 < colRight){
                int mid = (colRight - colLeft) / 2 + colLeft;
                int tmp = Integer.MIN_VALUE;
                int index = -1;
                for (int i = rowLeft; i <= rowRight; i++){
                    if (tmp < A[i][mid]){
                        tmp = A[i][mid];
                        index = i;
                    }
                }
                if (A[index][mid - 1] > A[index][mid]){
                    colRight = mid;
                }
                else if (A[index][mid + 1] > A[index][mid]){
                    colLeft = mid;
                }
                else{
                    r.add(index);
                    r.add(mid);
                    return r;
                }
            }
            flag = !flag;
        }

        if (check(A, rowLeft, colLeft)){
            r.add(rowLeft);
            r.add(colLeft);
        }
        else if (check(A, rowLeft, colRight)){
            r.add(rowLeft);
            r.add(colRight);
        }
        else if (check(A, rowRight, colLeft)){
            r.add(rowRight);
            r.add(colLeft);
        }
        else if (check(A, rowRight, colRight)){
            r.add(rowRight);
            r.add(colRight);
        }
        return r;
    }

    private boolean check(int[][] A, int x, int y){
        if (A[x - 1][y] < A[x][y]) return false;
        if (A[x + 1][y] < A[x][y]) return false;
        if (A[x][y - 1] < A[x][y]) return false;
        if (A[x][y + 1] < A[x][y]) return false;
        return true;
    }
}
