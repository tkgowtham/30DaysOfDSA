class MyStack(object):

    def __init__(self):
        self.q1 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.insert(0,x)
        for i in range(0, len(self.q1) - 1):
            self.q1.insert(0,self.q1.pop(0))

        

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return -1

        return self.q1.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.q1:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
