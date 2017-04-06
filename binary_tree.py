
# coding: utf-8

# In[1]:

class Node:
    def __init__(self, value):
        # payload this node will carry
        self.value = value
        # binary children nodes (left and right)
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        if self.value == data:
            # we are not allowing to insert same data twice
            return False
        elif self.value > data:
            # if the incoming data is SMALLER than the node's value
            if self.leftChild:
                # if left child node exists, insert into it
                return self.leftChild.insert(data) # recursive call
            else:
                # if left child does not exist, create new node
                self.leftChild = Node(data)
                return True
        else:
            # if the incoming data is BIGGER than the node's value
            if self.rightChild:
                # if right child node exists, insert into it
                return self.rightChild.insert(data) # recursive call
            else:
                # if right child does not exist, create new node
                self.rightChild = Node(data)
                return True
    
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data) # recursive
            else: 
                return False # not in the left branch
        else:
            # data must be BIGGER than stored value
            if self.rightChild:
                return self.rightChild.find(data) # recursive
            else: 
                return False # not in the right branch
            


# In[2]:

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
        
    def find(self, data):
        if self.root:
            return self.root.find(data) # recursive call
        else:
            return False # did not find node


# In[3]:

# TEST

tree = Tree()
tree.insert(5)


# In[4]:

assert(True == tree.find(5))


# In[5]:

assert(False == tree.find(6) )


# In[6]:

assert(True == tree.insert(6))


# In[7]:

assert(True == tree.find(6))


# In[8]:

assert(False == tree.find(4))


# In[9]:

assert(True == tree.insert(4))


# In[10]:

assert(True == tree.find(4))


# In[ ]:



