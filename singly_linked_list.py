class Node:
    '''
    This class is a helper class for building the nodes of
    the linked list
    '''
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def insert(self, val):
        self.next = Node(val)

class Singly_Linked_List():
    '''
    This class instantiates the singly linked list
    '''
    def __init__(self, val):
        self.head = Node(val)
    
