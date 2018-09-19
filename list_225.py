class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.queue) > 0:
            return self.queue.pop(-1)
        else:
            return -1

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return -1


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False



        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()

