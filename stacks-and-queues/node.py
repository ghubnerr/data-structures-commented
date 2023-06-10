# Singly Linked List Node for Stacks and Queue

class Node:
    def __init__(self, value) -> None:
        """Creates a node with no child using the value passed"""
        
        # This is the value that the Node itself will hold
        self.value = value 

        # This is the pointer to the next Node. It is set to None by default 
        self.next = None
