#!/usr/bin/env python
# coding: utf-8

# In[1]:


def countPalindrome(lb,ub):
    cnt = 0
    while lb != ub:
        # Implement
        if isPalindrome(lb) == True:
            cnt = cnt + 1
        lb = lb + 1
    return cnt
countPalindrome(1,10)


# In[2]:


n = int(input("Enter a Number :"))

ld = 0
while n > 0:
   r = n % 10
   if ld < r:
       ld = r
   n = int(n / 10)

print("\nLargest digit is :", ld)


# In[ ]:




