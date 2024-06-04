class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.insert(0,data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if len(self.arr) > 0:
            return self.arr.pop(0)
        else:
            return -1

''' Java Solution 

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

'''
