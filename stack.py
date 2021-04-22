class MyStack:
    '''
    Stack implementation using twp list data types as queues.
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.forward = []
        self.backward = []
        
    
    def _shuffle(self, forward=False) -> None:
        '''
        Move elements from forward queue to backward queue
        according to FIFO
        '''
        if forward:
            # move elements from forward to backward according to FIFO
            while len(self.forward) > 1:
                self.backward.append(self.forward[0])

                # deallocate memory provided to value
                del self.forward[0]
                
        else:
            # move elements from backward to forward according to FIFO
            while self.backward:
                self.forward.append(self.backward[0])

                # deallocate memory in backward queue
                del self.backward[0]
    
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.forward.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # move elements from forward queue to backward queue
        self._shuffle(forward=True)
        
        # grab element to pop
        val = self.forward[0]
        
        # deallocate memory provided to to_pop
        del self.forward[0]
        
        # move elements from backward queue to forward queue
        self._shuffle(forward=False)
        
        return val
        

    def top(self) -> int:
        """
        Get the top element.
        """
        # move elements from forward queue to backward queue
        self._shuffle(forward=True)

        # grab top element
        val = self.forward[0]
        del self.forward[0]
        
        # place element in backward queue
        self.backward.append(val)
        
        # move elements from backward queue to forward queue
        self._shuffle(forward=False)
        return val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.forward:
            return False
        else:
            return True        



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
