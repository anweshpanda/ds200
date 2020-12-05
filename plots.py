#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(io='Energy_data.xls')
x = np.arange(len(df))
y1 = df[df.keys()[1]].tolist()
y2 = df[df.keys()[2]].tolist()
y3 = df[df.keys()[3]].tolist()
y4 = df[df.keys()[4]].tolist()
y5 = df[df.keys()[5]].tolist()
y6 = df[df.keys()[6]].tolist()
plt.rcParams.update({'font.size': 20})
plt.figure(figsize =[20,12])
plt.bar(x,y1,width=0.1,label=df.keys()[1])
plt.bar(x+0.1,y2,width = 0.1,label=df.keys()[2])
plt.bar(x+0.2,y3,width = 0.1,label=df.keys()[3])
plt.bar(x+0.3,y4,width = 0.1,label=df.keys()[4])
plt.bar(x+0.4,y5,width = 0.1,label=df.keys()[5])
plt.bar(x+0.5,y6,width = 0.1,label=df.keys()[6])
plt.legend()

plt.xticks([i for i in range(len(df))],df[df.keys()[0]].tolist(),fontsize = 20)
plt.xlabel('Year',fontsize = 20)
plt.ylabel('Energy Used',fontsize = 20)
plt.title('Barplot for Yearly Use of Different Energies in India')
plt.savefig('barplot.png')


# In[33]:


df = pd.read_excel(io='Rain_data.xls')
data = [df[df.keys()[i]].tolist() for i in range(1,5)]
plt.figure(figsize = (20,15))
plt.rcParams.update({'font.size': 20})
plt.boxplot(data)
plt.xticks([i for i in range(1,5)],df.keys()[1:5],fontsize = 20)
plt.xlabel('Month',fontsize = 20)
plt.ylabel('Actaul Rainfall in cm',fontsize = 20)
plt.title('Boxplot for Monthly Rainfall in North-west from 1901 to 2016')
plt.savefig('boxplot.png')


# In[34]:


plt.figure(figsize=[15,10])
plt.rcParams.update({'font.size': 20})
plt.scatter(df[df.keys()[0]],df[df.keys()[1]],label = df.keys()[1])
plt.scatter(df[df.keys()[0]],df[df.keys()[2]],label = df.keys()[2])
plt.scatter(df[df.keys()[0]],df[df.keys()[3]],label = df.keys()[3])
plt.scatter(df[df.keys()[0]],df[df.keys()[4]],label = df.keys()[4])
plt.legend()
plt.xlabel('Year',fontsize = 20)
plt.ylabel('Actaul Rainfall in cm',fontsize = 20)
plt.title('Scatter plot Monthly Rainfall in North-west from 1901 to 2016')
plt.savefig('scatter.png')


# In[ ]:




