
# coding: utf-8

# # topcoder: Importance of Algorithims
# 
# https://www.topcoder.com/community/data-science/data-science-tutorials/the-importance-of-algorithms/
# 
# "Algorithms are optimized ways for accomplishing a given, well-defined task."

# # Big-O notations 
# 
# Big-O notations is also known as "the run time characteristic of an algorithm",as it describes the **runtime relative to the size of the input**.
# 
# For input size of N items it provides the worst-case runtime.
# 
# Below is the estimated completion time for 1 second (C = 1s) operation algorithm, where input items N = 100
# 
# - $O(Log(N))$	10-7 seconds 
# - $O(N)$	10-6 seconds 
# - $O(N*Log(N))$	10-5 seconds 
# - $O(N^2)$	10-4 seconds, i.e. runtime is proportional to the number of items squared
# - $O(N^6)$ 3 minutes 
# - $O(2^N)$	1014 years 
# - $O(N!)$	10142 years 

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



