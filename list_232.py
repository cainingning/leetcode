class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) > 0:
            return self.stack2.pop(-1)
        else:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop(-1))
            if len(self.stack2) > 0:
                return self.stack2.pop(-1)
            else:
                return -1

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) > 0:
            return self.stack2[-1]
        else:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop(-1))
            if len(self.stack2) > 0:
                return self.stack2[-1]
            else:
                return -1



    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return True
        else:
            return False



        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()

if __name__ == '__main__':
    queque = MyQueue()
    print(queque.push(1), queque.stack1, queque.stack2)
    print(queque.push(1), queque.stack1, queque.stack2)
    print(queque.peek(), queque.stack1, queque.stack2)
    print(queque.pop(), queque.stack1, queque.stack2)
    print(queque.pop(), queque.stack1, queque.stack2)
    print(queque.empty(), queque.stack1, queque.stack2)