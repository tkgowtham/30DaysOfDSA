class MyStack
{
    int top;
	int arr[] = new int[1000];

    MyStack()
	{
		top = -1;
	}
	
	//Function to push an integer into the stack.
    void push(int a)
	{
	    // Your code here
	    this.top++;
	    this.arr[this.top] = a;
	} 
	
    //Function to remove an item from top of the stack.
	int pop()
	{
        // Your code here
        if (top == -1) {
            return -1;
        } else {
            return this.arr[this.top--];
        }
	}
}
