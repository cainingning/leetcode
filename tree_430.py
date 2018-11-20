# Definition for a Node.

class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        tmp = [head]
        while len(tmp) > 0:
            pop_node = tmp.pop(-1)
            if pop_node.next:
                tmp.append(pop_node.next)
            if pop_node.child:
                tmp.append(pop_node.child)
            if len(tmp) > 0:
                pop_node.next = tmp[-1]
                tmp[-1].prev = pop_node
                pop_node.child = None


        return head

if __name__ == '__main__':
    solution = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.child = Node(4)
    head.next.child.next = Node(5)
    head = solution.flatten(head)
    while head:
        print(head.val)
        if head.prev:
            print('debug', head.prev.val)
        head = head.next
