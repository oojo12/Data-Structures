class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singly_Linked_List():
    def __init__(self, val):
        self.head = Node(val)
    
    def insert(self, val):
        self.next = Node(val)
