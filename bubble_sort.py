
# coding: utf-8

# In[1]:

# Bubble sort


# In[4]:

def bubble_sort(alist: list):
    temp_list = []
    
    # step backwards thru the list
    start = len(alist)-1
    stop = 0
    step = -1
    for passnum in range(start, stop, step):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [4,8,2,5,9,1,6,3,7]
bubble_sort(alist)
print(alist)


# In[ ]:



