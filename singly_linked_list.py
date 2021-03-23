class Node:
    def __init__(self):
        self.val = None
        self.next = None

class Singly_Linked_List():
    def __init__(self):
        self.head = Node()
    
    def insert(self, val):
        self.next = Node()
        self.next.val = val
