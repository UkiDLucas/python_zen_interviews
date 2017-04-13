
# coding: utf-8

# In[26]:

def print_directory_contents(dir_path, level=0):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    level = level + 1
    import os
    listing = os.listdir(dir_path) # returns list
    for item in listing:
        child_path = os.path.join(dir_path,item)
        print(level * "    " + child_path) # standard 4 spaces indent
        if os.path.isdir(item):
            print_directory_contents(child_path, level)
                        
    
print_directory_contents(".")


# In[ ]:



