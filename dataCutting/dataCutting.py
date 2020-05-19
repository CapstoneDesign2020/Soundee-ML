#!/usr/bin/env python
# coding: utf-8

# In[5]:


import librosa
import os
import numpy as np
import matplotlib.pyplot as plt
import glob


# In[4]:


#for문
# beginning of the vaccum cleaner
file_list =glob.glob('code/dataCutting/vaccum_cleaner/*')
print(file_list)


# In[12]:


file_id_list=[]
for wav in file_list:
    file_id_list.append(os.path.basename(wav))
print(file_id_list)


# In[16]:



for wav in file_list:
    if wav.endswith('.wav') :
        file_id=os.path.basename(wav)
        print(file_id)
        y,sr=librosa.load(wav,sr=16000)
        #time = np.linspace(0,len(y)/sr,len(y)) #time axis
        #original save
        #librosa.output.write_wav("original_"+file_id,y,sr)
    
        #cut half and save
        half = len(y)/2
        y2=y[:round(half)]
        #time2=np.linspace(0,len(y2)/sr,len(y2))
        librosa.output.write_wav("cut_"+file_id,y2,sr)


# In[6]:


#for문
#vaccum cleaner running
file_list =glob.glob('code/dataCutting/vaccum_cleaner_v1/*')
print(file_list)
file_id_list=[]
for wav in file_list:
    file_id_list.append(os.path.basename(wav))
print(file_id_list)

for wav in file_list:
    if wav.endswith('.wav') :
        file_id=os.path.basename(wav)
        print(file_id)
        y,sr=librosa.load(wav,sr=16000)
        #time = np.linspace(0,len(y)/sr,len(y)) #time axis
        #original save
        #librosa.output.write_wav("original_"+file_id,y,sr)
    
        #cut half and save
        half = len(y)/2
        y2=y[:round(half)]
        #time2=np.linspace(0,len(y2)/sr,len(y2))
        librosa.output.write_wav("cut_"+file_id,y2,sr)

