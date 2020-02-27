#!/usr/bin/env python
# coding: utf-8

# # Same Last Character

# In[ ]:


# Names of Partners: Pablo Morales Mendez, Aaron Varela, Drew Jacob


# In[1]:


sentence = "today is the last day of class"


# In[44]:


#sentence = "today is the last day of class"
#def same_last():
#    sentence.split("  ")
#    if index == -1:
#       print("true")
#    else:
#        print("false")

def same_last(str1, str2):
    if len(str1) - 1 == len(str2) -1:
        return 'true'
    else:
        return 'false'


# In[45]:


same_last('apple', 'rapple')


# In[47]:


same_last('cat', 'hat')


# In[61]:


#sentence = ""
#def same_last():
#    sentence.split("  ")
   # index == -1
#    if sentence.split("  ") == -1:
 #      return 'true'
 #   else:
  #      return 'false'


# # Counting Spaces

# In[35]:


saying = "I woke up today"


# In[63]:


len(saying.split()) - 1


# # Counting Nonspaces

# In[ ]:


saying = "Where's the leak ma'am"


# In[64]:


len(saying.split())


# # Removing Vowels

# In[ ]:


def devowel():

