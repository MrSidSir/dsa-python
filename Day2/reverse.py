# 1. Reverse a linked list iteratively
#  Workflow:
# Initialize prev=None, current=head. Loop till current becomes None, reverse pointers.
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

        def reverse(head):
            prev = Nonecurr = head
            while curr:
                nxt = curr.next 
                curr.next = prev
                prev = curr
                curr = nxt
                return prev
            
            # Real-world use: Implementing undo features in editors.
