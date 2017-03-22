
# coding: utf-8

# # Bubble sort

# In[1]:

perform_tests = True


# In[2]:

def bubble_sort(the_list: list, verbose: int=0):
    """
    This function changes the provided list.
    The list can contain integers, decimal numbers, strings, etc.
    The list is sorted in ascending order (first to last).
    The function does not return anything.
    """
    if verbose > 0:
        iteration = 0
    
    # count remining bubbles ( aka step backwards)
    start = len(the_list)-1 # end, zero-based list
    stop = 0 # beginning
    step = -1 # backwards
    for remaining_bubbles in range(start, stop, step):
        for i in range(remaining_bubbles):
            if verbose > 0:
                iteration = iteration + 1
                print("iteration", iteration, "remaining_bubbles", remaining_bubbles, "index", i) 
                print("  ", the_list)
                print("    comparing if is", the_list[i], "bigger than", the_list[i+1])
            if the_list[i] > the_list[i+1]:
                # swap
                temp = the_list[i+1] # temp placehoder for the value to be moved
                the_list[i+1] = the_list[i] # bubble up
                the_list[i] = temp # bubble down
    if verbose > 0:
        print("*** finished", len(the_list), "element list in ", iteration, "iterations")


# In[3]:

# EXAMPLES:
if perform_tests:
    
    my_list = ["gamma", "alfa", "beta", "kappa"]
    bubble_sort(my_list, verbose = 1)
    print(my_list)


# In[4]:

# EXAMPLES:
if perform_tests:
    

    my_list = [4,8,2,5,9,1,6,3,7]
    bubble_sort(my_list, verbose=0)
    print(my_list)


# In[5]:

# EXAMPLES:
if perform_tests:
    

    my_list = [4.6,8.1,2.7,5.3,9,1,6,3,7]
    bubble_sort(my_list)
    print(my_list)

    my_list = ["c", "a", "b", "d"]
    bubble_sort(my_list)
    print(my_list)


    my_list = ["gamma", "alfa", "betta", "kappa"]
    bubble_sort(my_list)
    print(my_list)


# In[6]:

# CORNER CASEES
if perform_tests:
    my_list = [] # empty list
    bubble_sort(my_list)
    print(my_list)


# In[ ]:



