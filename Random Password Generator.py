#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16

password = "".join(random.sample(total, length))

print(password)
