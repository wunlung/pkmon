#!/usr/bin/env python
# coding: utf-8

# In[1]:


for x in [0, 1, 2]:
  pass


# In[2]:




for r in range(1,5):
    for c in range (1,r+1):
        print c,
    print


# In[3]:




for r in range(1,6):
    for c in range (1,r+1):
        print (c)
        print


# In[4]:


for r in range(1,6):
    for c in range (1,r+1):
        print (c)
        
        for r in range(1,6):
    for c in range (1,r+1):
        print (c)
        print


# In[5]:


def a(n):
    num=1 
    for i in range (0,n):
        num=1
      
        for j in range (0,i+1):
            
           
            print(num ,end=" ")
            
        
         
            num=num+1
        print("\r")
n=5
a(n)


# In[6]:


n=int(input("enter n value:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end="" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(chr(65+j),end=" ")
    print()


# In[7]:


n=int(input("enter n value:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(chr(65+j),end=" ")
    print()


# In[8]:


n=int(input("enter n value:"))
for i in range(n):
    for j in range(i+1):
        print(int(65+j),end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(int(65+j),end=" ")
    print()


# In[9]:


n=int(input("enter n value:"))
for i in range(n):
    for j in range(i+1):
        print(int(65+j),end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(int(65+j),end=" ")
    print()


# In[10]:


n=int(input("enter n value:"))
for i in range(n):
    for j in range(i+1):
        print(int(1+j),end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(int(1+j),end=" ")
    print()


# In[ ]:




