class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.my_stack = []
        self.min_stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x is None:
            return
        self.my_stack.append(x)
        if len(self.min_stk) == 0 or x < self.min_stk[-1]:
            self.min_stk.append(x)
        else:
            self.min_stk.append(self.min_stk[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.my_stack.pop(-1)
        self.min_stk.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self.my_stack) == 0:
            return -1
        return self.my_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stk) == 0:
            return -1
        return self.min_stk[-1]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()