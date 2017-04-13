
# coding: utf-8

# In[1]:

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)
print(sorted(A0)) # same as .keys
print(sorted(A0.values() ))


# In[2]:

A1 = range(10)
print(A1)


# In[3]:

A2 = sorted([i for i in A1 if i in A0])
print(A2)


# In[4]:

A3 = sorted([A0[s] for s in A0])
print(A3)


# In[5]:

A4 = [i for i in A1 if i in A3]
print(A4)


# In[6]:

A5 = {i:i*i for i in A1}
print(A5)


# In[7]:

A6 = [[i,i*i] for i in A1]
print(A6)


# In[ ]:



