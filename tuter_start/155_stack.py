class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.my_stack = []
        self.my_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.my_stack.append(x)
        if len(self.my_min) > 0:
            self.my_min.append(min(self.my_min[-1], x))
        else:
            self.my_min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.my_stack) > 0:
            self.my_stack.pop(-1)
            self.my_min.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self.my_stack) > 0:
            return self.my_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.my_min) > 0:
            return self.my_min[-1]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()