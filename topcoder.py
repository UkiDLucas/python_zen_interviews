
# coding: utf-8

# # TopCoder: Importance of Algorithims
# 
# https://www.topcoder.com/community/data-science/data-science-tutorials/the-importance-of-algorithms/
# 
# "Algorithms are optimized ways for accomplishing a given, well-defined task."

# # Big-O notation
# 
# Big-O notations is also known as "the run time characteristic of an algorithm",as it describes the **runtime relative to the size of the input**.
# 
# For input size of N items it provides the worst-case runtime.
# 
# A computer can easily complete 100 operations per second.
# 
# 
# references:
# - https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/

# In[1]:

N = 1000 # input size
C = 1 # execution time per operation 1 second


# Below is the estimated completion time for 1 second (C = 1s) operation algorithm, where input items N = 100
# 
# - $O(Log(N))$	10-7 seconds 
# - $O(1)$ 1.001 second
# - $O(N)$	10-6 seconds 
# - $O(N*Log(N))$	10-5 seconds 
# - $O(N^2)$	10-4 seconds, i.e. runtime is proportional to the number of items squared
# - $O(N^6)$ 3 minutes 
# - $O(2^N)$	1,014 years 
# - $O(N!)$	10,142 years 

# In[2]:

class TimeIt():
    from datetime import datetime
    def __enter__(self):
        self.start = self.datetime.now()
    def __exit__(self, *args, **kwargs):
        self.measured = self.datetime.now() - self.start
        #print('runtime: {}'.format(self.measured))
        times.append(self.measured.microseconds)


# In[3]:

import numpy
import timeit

sample_set = numpy.random.randint(low=0, high=N, size=N, dtype='l')

print(len(sample_set))

times = []

with TimeIt():
    print("sample_set:\n", sample_set[0:10])
with TimeIt():
    print("sorted sample_set:\n", sorted(sample_set)[0:10])
with TimeIt():
    print("sample_set:\n", sample_set[0:10])
with TimeIt():
    print("sorted sample_set:\n", sorted(sample_set)[0:10])


# In[4]:

def plot_results(sizes, times):
    import numpy as np
    logs = np.log10(sizes)
    import matplotlib
    import matplotlib.pyplot as plt
    
    sizes_times, = plt.plot(sizes, times, ".b", label='Line 2') # blue dots
    sizes_logs, = plt.plot(sizes, logs, "y", label='Line 2') # yellow line
    
    max_y = max(times)
    import math
    max_x = math.sqrt(max_y)
    quadratic_x = np.linspace(0, max_x, 10)
    quadratic_y = []

    for value in quadratic_x:
        quadratic_y.append(value*value)
        
    sizes_quadratic, = plt.plot(quadratic_x, quadratic_y, "r", label='Line 2') # yellow line

    plt.legend([sizes_times, sizes_logs, sizes_quadratic], ['size vs time', 'size log(10)', "size^2"])

    plt.ylabel('sample size')
    plt.xlabel('microseconds')
    #plt.axis([0, 6, 0, 20]) # axis spans
    #plt.figure(figsize=(20,10))
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    #fig.savefig('test2png.png', dpi=100)
    plt.show()


# In[5]:

def time_function(my_function):
    times = []
    sizes = []
    for sample_size in range(0, N, 20):  
        sizes.append(sample_size)
        with TimeIt():
            x = my_function(listing = sample_set[0:sample_size + 1])
            print (sample_size, "sample_size produced first element =", x)

    print("times in microseconds\n",times)
    print("sizes\n",sizes)

    plot_results(sizes, times)


# ## $O(1)$ 
# 
# executes the same amount of time regardless on input size, also noted a C.

# In[6]:

import time

def return_first_element(listing: list):
    #time.sleep(C)
    return listing[0]

times = []
sizes = []
for sample_size in range(0, N, 20):  
    sizes.append(sample_size)
    with TimeIt():
        x = return_first_element(listing = sample_set[0:sample_size + 1])
        #print (sample_size, "sample_size produced first element =", x)
    
print("times in microseconds\n",times)
print("sizes\n",sizes)

plot_results(sizes, times)


# # $O(N)$
# 
# Performance grows linearly in direct proportion to the size of the input data set

# In[7]:

value = sample_set[-1] # last element
#print(sample_set)
print(value) 

def find_value(elements: list, value: str):
    for item in elements:
        if (item == value): 
            return True
    return False



times = []
sizes = []
for sample_size in range(0, N, 20):  
    sizes.append(sample_size)
    
    current_set = sample_set[0:sample_size + 1]
    value = current_set[-1] # last value in the set
    
    with TimeIt():
        x = find_value(current_set, value)
        #print (sample_size, "sample_size produced first element =", x)
    
print("runtime in microseconds:\n",times)
print("data set size:\n",sizes)

plot_results(sizes, times)


# In[8]:

def find_first(array: list, value):
    """
    Returns ferst index of the first location where velue was found.
    """
    indexes = numpy.where(array == value)
    #print(indexes) # e.g. (array([  0, 444, 599]),)
    return indexes[0][0] # first element
    
#print(find_first(sample_set, 409))


# # $O(N2)$
# 
# Proportional to sqare of number of input values.
# Double iteration loop.

# In[9]:

def find_duplicates(listing: list):
    #print(type(listing))
    has_found = False
    for index_outer in range(0, len(listing)):
        for index_inner in range(0, len(listing)):
            if index_outer != index_inner: # do not compare to self
                outer = listing[index_outer]
                inner = listing[index_inner]
                if (outer == inner):
                    #print(outer, index_outer, inner,index_inner)
                    #return True # we want worse case scenario
                    has_found = True
    return has_found

find_duplicates(sample_set)


times = []
sizes = []
for sample_size in range(0, N, 20):  
    sizes.append(sample_size)
    
    current_set = sample_set[0:sample_size + 1]
    #value = current_set[-1] # last value in the set
    
    with TimeIt():
        find_duplicates(current_set)
    
print("runtime in microseconds:\n",times)
print("data set size:\n",sizes)

plot_results(sizes, times)


# 

# # Coding
# 
# You should know at least one programming language really well (preferably C++,  Java or Python). You will be expected to write some code in at least some of your interviews. You will be expected to know a fair amount of detail about your preferred programming language and will be asked to do some coding on the whiteboard.

# # Hashtables
# 
# Arguably the single most important data structure known to mankind. You absolutely should know how they work. Be able to implement one using only arrays in your favorite language, in about the space of one interview.

# # Sorting
# 
# Know how to sort. Don't do bubble-sort. You should know the details of at least one n*log(n) sorting algorithm, preferably two (say, quicksort and merge sort). Merge sort can be highly useful in situations where quick sort is impractical, so take a look at it.

# # Trees
# 
# Know about trees; basic tree construction, traversal and manipulation algorithms. Familiarize yourself with binary trees, n-ary trees, and trie-trees. Be familiar with at least one type of balanced binary tree, whether it's a red/black tree, a splay tree or an AVL tree, and know how it's implemented. Understand tree traversal

# # Other Data Structures
# 
# You should study up on as many other data structures and algorithms as possible. You should especially know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem, and be able to recognize them when an interviewer asks you them in disguise. Find out whatNP-complete means.

# # Algorithms
# 
# BFS and DFS, and know the difference between inorder, postorder and preorder.
# Graphs: Graphs are really important at Google. There are 3 basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list); familiarize yourself with each representation and its pros & cons. You should know the basic graph traversal algorithms: breadth-first search and depth-first search. Know their computational complexity, their tradeoffs, and how to implement them in real code. If you get a chance, try to study up on fancier algorithms, such as Dijkstra and A*.
# 
# You may want to refresh hash tables, heaps, binary trees, linked lists, depth-first search, recursion. For more information on Algorithms you can visit:
# http://www.topcoder.com/tc?module=Static&d1=tutorials&d2=alg_index

# # Mathematics
# 
# Some interviewers ask basic discrete math questions. This is more prevalent at Google than at other companies because counting problems, probability problems, and other Discrete Math 101 situations surrounds us. Spend some time before the interview refreshing your memory on (or teaching yourself) the essentials of combinatorics and probability. You should be familiar with n-choose-k problems and their ilk – the more the better.

# # Operating Systems
# 
# Know about processes, threads and concurrency issues. Know about locks and mutexes and semaphores and monitors and how they work. Know about deadlock and livelock and how to avoid them. Know what resources a processes needs, and a thread needs, and how context switching works, and how it's initiated by the operating system and underlying hardware. Know a little about scheduling. The world is rapidly moving towards multi-core, so know the fundamentals of "modern" concurrency constructs. For information on System Design:
# http://research.google.com/pubs/DistributedSystemsandParallelComputing.html

# In[ ]:



