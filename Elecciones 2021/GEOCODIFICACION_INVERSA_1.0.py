#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import os
import time


# In[ ]:


import numpy as np


# In[ ]:


from geopy.point import Point  


# In[2]:


os.chdir('C:/Users/diego/OneDrive/Escritorio/Campaña//')


# In[1]:


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="sample app")


# In[ ]:


#GEOLOCALIZACION INVERSA(COORDENADAS CARTESIANAS A DOM )


# In[ ]:


with open('Padrón_Ausentes_Cordenadas.csv') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',', quotechar='\'')
    with open('Padrón de ausentes con direccion.xlsx','w') as csv_aux:
        name_csv=['Apellidos','Nombres','Año','Edad','Dni','Domicilio']
        writer= csv.DictWriter(csv_aux,fieldnames=name_csv, delimiter=',')   
        writer.writeheader()
        for row in csv_data: 
            lat=row[5]
            lon=row[6] 
            #print('{},{}'.format(lat,lon))
            aux= ('{},{}'.format(lat,lon))
            #p=Point(lat,lon)
            print(aux)
            loc=geolocator.reverse(Point(aux)) 
            #loc=geolocator.reverse(f'{lat},{lon}') 

