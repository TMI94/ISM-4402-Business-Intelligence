#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']

df['lettergrade'] = pd.cut(df['grade'], bins,
 labels=group_names)
df

pd.value_counts(df['lettergrade'])

# Create the bin dividers
bins = [0, 80, 100]
# Create names for the two groups
group_names = ['Fail', 'Pass']

df['pass/fail'] = pd.cut(df['grade'], bins,
 labels=group_names)
df


# In[ ]:




