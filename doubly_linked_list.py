'''
Class requires user to update the head reference on inserts
'''
class Node:
    def __init__(self, curr_val, prev_val):
        self.val = curr_val
        self.next = None
        if prev_val is not None:
            self.prev = prev_val
    
    def insert(self, val):
        self.next = Node(val, prev_val=self)

class Doubly_Linked_List():
    def __init__(self, val):
        self.head = Node(val, None)
    
