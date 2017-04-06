
# coding: utf-8

# In[ ]:

class Node:
    def __init__(self, value):
        # payload this node will carry
        self.value = value
        # binary children nodes (left and right)
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.value == data:
            # we are not allowing to insert same data twice
            return False
        elif self.value > data:
            # if the existing data bigger than new data
            if self.leftChild:
                # if left child node exists, insert into it
                return self.leftChild.insert(data)
            else
                # if left child does not exist, create new node
                self.leftChild = Node(data)
                return True
            
            
class Tree:
    def __init__(self):
        # start empty
        self.root = None
        
    def insert(self, data):
        if self.root:
            # if it has root, then we insert data into the root
            return self.root.insert(data) # True or False
        else:
            # if it does not have a root node, create a new Node
            self.root = Node(data)
            return True
        

