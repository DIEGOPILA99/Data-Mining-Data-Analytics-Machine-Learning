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


# In[1]:


total_capturados=0
total_no_capturados=0
with open('Padrón de ausentes con direccion.xlsx - Hoja.csv', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',', quotechar='\'')
    with open('Padrón_Ausentes_Cordenadas.csv','w') as csv_aus:
        name_csv=['Apellidos','Nombres','Año','Edad','Dni','Lat','Long']
        writer= csv.DictWriter(csv_aus,fieldnames=name_csv, delimiter=',')   
        writer.writeheader()
        with open('Padrón_Ausentes_Cordenadas_No_Calculables.csv','w') as csv_aus2:
            name_csv2=['Apellidos','Nombres','Año','Edad','Dni','Domicilio']
            writer2= csv.DictWriter(csv_aus2,fieldnames=name_csv2, delimiter=',')   
            writer2.writeheader()
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
                        #print(persona)  
                        writer.writerow(persona)
                        total_capturados+=1
                    else:
                        apellido=row[2]
                        nombre=row[3]
                        fec=row[4]
                        edad=row[5]
                        dni=row[6]
                        dom=row[7]
                        persona2={'Apellidos':apellido, 'Nombres':nombre, 'Año':fec, 'Edad':edad,'Dni':dni,'Domicilio':dom}
                        #(persona2)  
                        writer2.writerow(persona2)
                        total_no_capturados+=1
print('la cantidad de domicilios fueron convertidos son: '+total_capturados)
print('la cantidad de domicilios que no fueron convertidos son: '+total_no_capturados)


# In[ ]:


#MIRARA


# In[17]:


with open('Padrón de ausentes con direccion.xlsx - Hoja1.csv', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    with open('Padrón_Ausentes_Cordenadas.csv','w') as csv_aus:
        name_csv=['Apellidos','Nombres','Año','Edad','Dni','Lat','Long']
        #writer= csv.DictWriter(csv_aus,fieldnames=name_csv, delimiter=',', quotechar=' '')
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
                    writer2.writerow(persona)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


with open('Padrón de ausentes con direccion.xlsx - Hoja2.csv', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',', quotechar='\'')
    with open('Padrón_Ausentes_Cordenadas.csv','a') as csv_aus:
        name_csv=['Apellidos','Nombres','Año','Edad','Dni','Lat','Long']
        writer= csv.DictWriter(csv_aus,fieldnames=name_csv, delimiter=',', quotechar='\'')
        writer.writeheader()
        for row in csv_data:  
            print('hola')
            print(row)
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


# In[ ]:


with open('Padrón de ausentes con direccion.xlsx - Hoja2.csv', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',', quotechar='\'')
    for row in csv_data:  
        geodir = geolocator.geocode('{},Pila,Buenos Aires,Argentina'.format(row[7]), timeout=None)
        if(geodir!=None):
                print(row[2], row[3], row[7])
                aux=[row[2],row[3],row[4],row[5],row[6],geodir.raw.get('lat'),geodir.raw.get('lon')]
                writer.writerow(aux)

