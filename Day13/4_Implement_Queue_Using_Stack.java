class MyQueue {

    int stack1[] = new int[10000];
    int stack2[] = new int[10000];
    int top1;
    int top2;

    public MyQueue() {
        this.top1 = -1;
        this.top2 = -1;
    }
    
    public void push(int x) {
        this.stack1[++this.top1] = x;
    }
    
    public int pop() {
        if (this.top2 == -1) {
            while (this.top1 != -1) {
                this.stack2[++top2] = stack1[top1--];
            }
        }

        return this.stack2[top2--];
    }
    
    public int peek() {
        if (this.top2 == -1) {
            while (this.top1 != -1) {
                this.stack2[++top2] = stack1[top1--];
            }
        }

        return this.stack2[top2];
    }
    
    public boolean empty() {
        if (this.top1 == -1 && this.top2 == -1) {
            return true;
        } else {
            return false;
        }
    }
}
