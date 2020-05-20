#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydub import AudioSegment
import glob
import os


# In[6]:


# dcase2018 watersound in class dishwashing (meat-labeling.xlsx - dishwashing-d2)
file_list =glob.glob('dataCutting/water/dcase2018_washdishing_d2/*')
print(file_list)


# In[8]:


for wav in file_list:
    if wav.endswith('.wav') :
        file_id=os.path.basename(wav)
        print(file_id)
        original = wav=AudioSegment.from_wav(wav)
        #pydub는 milliseconds 단위를 사용한다
        t1=0*1000
        t2=5*1000
        t3=10*1000
        front_wav= wav[t1:t2]
        front_wav.export('front'+file_id,format="wav")
        backWav= wav[t2:t3]
        backWav.export('back'+file_id,format="wav")


# In[23]:


#wav=AudioSegment.from_wav("dataCutting/water/dcase2018_washdishing_d2/DevNode3_ex62_1.wav")

