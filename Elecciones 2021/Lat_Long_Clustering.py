#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os
import time


# In[2]:


#IMPORT LIBRARY'S TO MANIPULATION


# In[3]:


import numpy as np
import pandas as pd


# In[4]:


#


# In[5]:


os.chdir('C:/Users/diego/OneDrive/Escritorio/Proyectos para Git/Elecciones 2021//')
#os.chdir('../Elecciones 2021//')


# In[6]:


#ACCESS DATAFRAME


# In[7]:


data=pd.read_csv('Padrón_Ausentes_Cordenadas.csv',encoding='ISO-8859-1')


# In[8]:


data.head()


# In[ ]:


mean_lat=data["Lat"].mean()
mean_lon=data["Long"].mean()


# In[ ]:


print(mean_lat)
print(mean_lon)


# In[ ]:


std_lat=data["Lat"].std()
std_lon=data["Long"].std()


# In[ ]:


data["Lat"]=(data["Lat"] - mean_lat)/(std_lat) 
data["Long"]=(data["Long"] -mean_lon ) /(std_lon)


# In[ ]:


data.head()


# In[9]:


#IMPORT LIBRARY'S TO K-MEANS 


# In[10]:


from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans


# In[11]:


#DATA PRERARETION TO K-MEANS


# In[12]:


x=data['Lat'].values
y=data['Long'].values
X=np.array(list(zip(x,y)))


# In[13]:


n_sil=[]
n=0
for n in range(1,5):
    kmeans= KMeans(n_clusters=2*n, random_state=1).fit(X)
    labels =kmeans.predict(X)
    aux=metrics.silhouette_score(X,labels, metric='euclidean')
    n_sil.append([n,aux])


# In[ ]:





# In[14]:


for n in range(0,len(n_sil)):
    print(n_sil[n])


# In[15]:


max_sil=-999
max_sil2=-999
max_clus=-999
max_clus2=-999
for n in range(0,len(n_sil)):
    if( (max_sil<n_sil[n][1]) ):
            max_sil2=max_sil
            max_clus2=max_clus 
            max_sil=n_sil[n][1]
            max_clus=2*(n+1)
    else:
        if( (max_sil2<n_sil[n][1]) ):
            max_sil2=n_sil[n][1]
            max_clus2=2*(n+1)        


# In[16]:


print('el cluster con n={} posee el mejor ind de sillhoute con s={}'.format(max_clus,round(max_sil,8)))
print('el cluster con n={} posee el segundo mejor ind de sillhoute con s={}'.format(max_clus2,round(max_sil2,8)))


# In[17]:


#Since we have at least 12 people in our team, 
#we prefer to lose performance in geographical 
#density and divide the work


# In[18]:


#We apply K-means wit N_Clusters=max_clus2=6


# In[19]:


import matplotlib.pyplot as plt


# In[20]:


print(max_clus2)


# In[29]:


#kmeans=KMeans(n_clusters=max_clus2)
kmeans=KMeans(n_clusters=max_clus2)
kmeans=kmeans.fit(X)
labels = kmeans.predict(X)
centroids=kmeans.cluster_centers_
colors=['m.','r.','c.','y.','b.','.']


# In[30]:


X.shape


# In[33]:


for i in range(len(X)):
    print('lat y log:',X[i],' grupo: ',labels[i])
    plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=50)
plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=50,linewidth=5,zorder=10)
plt.show()


# In[ ]:





# In[ ]:




