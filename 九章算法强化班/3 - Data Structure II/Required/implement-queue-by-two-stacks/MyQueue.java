import java.util.*;

public class MyQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    private boolean state;

    public MyQueue() {
        // do initialization if necessary
        this.state = false;
        this.stack1 = new Stack<Integer>();
        this.stack2 = new Stack<Integer>();
    }

    private void reverse(){
        if (stack2.size() > 0){
            while (stack2.size() > 0){
                stack1.push(stack2.pop());
            }
        }
        else{
            while (stack1.size() > 0){
                stack2.push(stack1.pop());
            }
        }

        state = !state;
    }

    public void push(int element) {
        // write your code here
        if (state){
            reverse();
        }
        stack1.push(element);
    }

    public int pop() {
        // write your code here
        if (!state){
            reverse();
        }
        return stack2.pop();
    }

    public int top() {
        // write your code here
        if (!state){
            reverse();
        }
        return stack2.peek();
    }
}