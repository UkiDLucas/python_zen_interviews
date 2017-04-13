
# coding: utf-8

# In[46]:

def print_directory_contents(dir_path: str="."):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    If provided dir_path does not exist it throws:
    FileNotFoundError: [Errno 2] No such file or directory: 'x'
    """
    import os # consecutive calls are fast

    for item in os.listdir(dir_path): # returns a list
        item_path = os.path.join(dir_path, item) # system specific separator
        print(item_path) # standard 4 spaces indent
        
        if os.path.isdir(item_path): # recursive, do same for sub dir
            print_directory_contents(item_path)

                        
    
print_directory_contents(".") # careful where you call it, you could wait a long time


# In[ ]:



