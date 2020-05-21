#!/usr/bin/env python
# coding: utf-8

# In[23]:


import librosa
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from pydub import AudioSegment


# In[54]:


#초로 구분되어있는 폴더불러오기
file_list_00s=glob.glob('dataCutting/dropping_object/vol87_drop_object_sound_effects/0s/*')
file_list_01s=glob.glob('dataCutting/dropping_object/vol87_drop_object_sound_effects/1s/*')
file_list_02s=glob.glob('dataCutting/dropping_object/vol87_drop_object_sound_effects/2s/*')
file_list_03s=glob.glob('dataCutting/dropping_object/vol87_drop_object_sound_effects/3s/*')
file_list_04s=glob.glob('dataCutting/dropping_object/vol87_drop_object_sound_effects/4s/*')


# In[55]:


#silence sound 불러오기
silence05=AudioSegment.from_wav('dataCutting/silence/5_silence.wav')
silence04=AudioSegment.from_wav('dataCutting/silence/4_silence.wav')
silence03=AudioSegment.from_wav('dataCutting/silence/3_silence.wav')
silence02=AudioSegment.from_wav('dataCutting/silence/2_silence.wav')
silence01=AudioSegment.from_wav('dataCutting/silence/1_silence.wav')


# In[29]:


# 1초짜리 폴더 돌리기
"""
for wav in file_list_01s:
    if wav.endswith('.wav') :
        file_id=os.path.basename(wav)
        print(file_id)
        original=AudioSegment.from_wav(wav)
        add_silence_wav=original+silence04
        add_silence_wav.export('add_silence'+file_id,format="wav")
"""       
       


# In[52]:


#함수로 구현
def addSilenceWav(file_list,silence):
    for wav1 in file_list:
        if wav1.endswith('.wav') :
            file_id=os.path.basename(wav1)
            print(file_id)
            original=AudioSegment.from_wav(wav1)
            add_silence_wav=original+silence
            add_silence_wav.export('add_silence'+file_id,format="wav")
    


# In[56]:


addSilenceWav(file_list_00s,silence05)
addSilenceWav(file_list_01s,silence04)
addSilenceWav(file_list_02s,silence03)
addSilenceWav(file_list_03s,silence02)
addSilenceWav(file_list_04s,silence01)


# In[ ]:




