#!/usr/bin/env python
# coding: utf-8

# In[8]:


#basic library  


# In[9]:


import csv
import os
import time


# In[10]:


import numpy as np


# In[11]:


#basic base addres csv 


# In[12]:


os.chdir('C:/Users/diego/OneDrive/Escritorio/Campaña//')


# In[ ]:


#basic library to transform addresses into coordinates


# In[13]:


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="sample app")


# In[ ]:


#FUNCIONA NO TOCAR


# In[ ]:


with open('Padrón de ausentes con direccion.xlsx - Hoja1.csv', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',', quotechar='\'')
    with open('Padrón_Ausentes_Cordenadas.csv','w') as csv_aus:
        name_csv=['Apellidos','Nombres','Año','Edad','Dni','Lat','Long']
        writer= csv.DictWriter(csv_aus,fieldnames=name_csv, delimiter=',')   
        writer.writeheader()
        for row in csv_data:  
                print('hola')
                geodir = geolocator.geocode('{},Pila,Buenos Aires,Argentina'.format(row[7]), timeout=None)
                if(geodir!=None):
                    lat=geodir.raw.get('lat')
                    lon=geodir.raw.get('lon')
                    #if(lat!=None):
                     #if(lon!=None):
                    print(row[2], row[3], row[7])
                    apellido=row[2]
                    nombre=row[3]
                    fec=row[4]
                    edad=row[5]
                    dni=row[6]
                    persona={'Apellidos':apellido, 'Nombres':nombre, 'Año':fec, 'Edad':edad,'Dni':dni,'Lat':lat,'Long':lon}
                    print(persona)  
                    writer.writerow(persona)

