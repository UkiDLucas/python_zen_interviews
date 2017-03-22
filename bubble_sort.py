
# coding: utf-8

# # Bubble sort

# 

# In[8]:

def bubble_sort(alist: list):
    print("elements to sort", len(alist))
    temp_list = []
    iteration = 0
    
    # step backwards thru the list
    start = len(alist)-1
    stop = 0
    step = -1
    for placeholder in range(start, stop, step):
        for i in range(placeholder):
            iteration = iteration + 1
            print("iteration", iteration, "placeholder", placeholder, "index", i)
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [4,8,2,5,9,1,6,3,7]
bubble_sort(alist)
print(alist)


# In[ ]:



