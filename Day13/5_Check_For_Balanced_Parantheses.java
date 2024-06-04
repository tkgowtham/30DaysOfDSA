class stack{
    char arr[] = new char[10000];
    int top;
    public stack(){
        this.top = -1;
    }

    public void push(char x){
        this.arr[++this.top] = x;
    }

    public char pop() {
        if (top == -1)
            return '1';

        return this.arr[this.top--];
    }
}

class Solution {
    public boolean isValid(String s) {
        stack st = new stack();
        for (char ch : s.toCharArray()){
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            } else {
                char v = st.pop();
                if (v == '(' && ch == ')') {
                    continue;
                } else if (v == '{' && ch == '}') {
                    continue;
                } else if (v == '[' && ch == ']') {
                    continue;
                } else {
                    return false;
                }
            }
        }

        if (st.pop() == '1')
            return true;
        else
            return false;
    }
}
