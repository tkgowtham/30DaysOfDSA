//Using One Queue
class MyStack {

        int q1[]= new int[100000];
        int front1;
        int rear1;

    public MyStack() {
        front1 = 0;
        rear1 = 0;
    }
    
    public void push(int x) {
        this.q1[this.rear1++] = x;
        int temp = this.rear1 - this.front1 - 1;
        for (int i = 0; i < temp; i++) {
            this.q1[this.rear1++] = this.q1[this.front1++]; 
        }
    }
    
    public int pop() {
        if (empty()) {
            return -1;
        }

        return this.q1[this.front1++];
    }
    
    public int top() {
        if (this.front1 == this.rear1) {
            return -1;
        }
        return this.q1[front1];
    }
    
    public boolean empty() {
        if (this.front1 == this.rear1) {
            return true;
        } else {
            return false;
        }
    }
}


//Using two queues
class MyStack {

        int q1[]= new int[100000];
        int q2[] = new int[100000];
        int front1;
        int front2;
        int rear1;
        int rear2 ;

    public MyStack() {
        front1 = 0;
        front2 = 0;
        rear1 = 0;
        rear2 = 0;
    }
    
    public void push(int x) {
        this.q1[this.rear1++] = x;
    }
    
    public int pop() {
        if (empty()) {
            return -1;
        }

        while (this.front1 < this.rear1 - 1) {
            this.q2[this.rear2++] = this.q1[this.front1++];
        }

        int val = this.q1[this.front1++];

        while (this.front2 != this.rear2) {
            this.q1[this.rear1++] = this.q2[this.front2++];
        }

        return val;
    }
    
    public int top() {
        if (this.front1 == this.rear1) {
            return -1;
        }

        int val = pop();
        push(val);
        return val;
    }
    
    public boolean empty() {
        if (this.front1 == this.rear1) {
            return true;
        } else {
            return false;
        }
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
