class Pair{
    public int index = 0;
    public int result = 0;

    public Pair(int index, int result){
        this.index = index;
        this.result = result;
    }
}

public class ConnectingGraph2 {

    private int[] father = null;

    public ConnectingGraph2(int n) {
        // initialize your data structure here.
        father = new int[n];
        for(int i = 0; i < n; i++){
            father[i] = -1;
        }
    }

    private Pair find(int a){
        if (father[a] < 0){
            return new Pair(a, father[a]);
        }
        Pair r = find(father[a]);
        father[a] = r.index;
        return r;
    }

    public void connect(int a, int b) {
        // Write your code here
        Pair a_f = find(a - 1);
        Pair b_f = find(b - 1);
        if (a_f.index != b_f.index){
            father[a_f.index] = a_f.result + b_f.result;
            father[b_f.index] = a_f.index;
        }
        // System.out.println(Arrays.toString(father));
    }

    public int query(int a) {
        // Write your code here
        return -find(a - 1).result;
    }
}