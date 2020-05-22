#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pydub import AudioSegment
import glob
import os


# In[3]:


# dcase2018 watersound in class dishwashing (meat-labeling.xlsx - dishwashing-d2)
file_list =glob.glob('dataCutting/water/dcase2018_washdishing_d2/*')
print(file_list)


# In[4]:


for wav in file_list:
    if wav.endswith('.wav') :
        file_id=os.path.basename(wav)
        print(file_id)
        original = AudioSegment.from_wav(wav)
        #pydub는 milliseconds 단위를 사용한다
        t1=0*1000
        t2=5*1000
        t3=10*1000
        front_wav= original[t1:t2]
        front_wav.export('front'+file_id,format="wav")
        backWav= original[t2:t3]
        backWav.export('back'+file_id,format="wav")


# In[23]:


#wav=AudioSegment.from_wav("dataCutting/water/dcase2018_washdishing_d2/DevNode3_ex62_1.wav")


# In[ ]:


# dropping object sound custom cut

#Vol.87 Drop Objects Sound Effects


# In[31]:


def cuttingBasedOnTime(wav,a,b):
    original = AudioSegment.from_wav(wav)
    file_id=os.path.basename(wav)
    t1=a*1000
    t2=b*1000
    cut_wav=original[t1:t2]
    cut_wav.export('cut0'+str(b-a)+'_'+str(a)+'_'+file_id,format="wav")
    


# In[32]:


# 13
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/13. Hammer Drop by sagetyrtle Id-75307.wav",0,2)
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/13. Hammer Drop by sagetyrtle Id-75307.wav",2,6)
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/13. Hammer Drop by sagetyrtle Id-75307.wav",6,8)


# In[42]:


#30
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/30. Key Pick Up Drop by LamaMakesMusic Id-403582.wav",0,3)
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/30. Key Pick Up Drop by LamaMakesMusic Id-403582.wav",4,9)
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/30. Key Pick Up Drop by LamaMakesMusic Id-403582.wav",7,10)


# In[47]:


#10
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/10. Dropping Bag Of Bread by qubodup Id-189312.wav",0,2)
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/10. Dropping Bag Of Bread by qubodup Id-189312.wav",2,5)
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/10. Dropping Bag Of Bread by qubodup Id-189312.wav",2,6)
cuttingBasedOnTime("dataCutting/dropping_object/Vol.87 Drop Objects Sound Effects/10. Dropping Bag Of Bread by qubodup Id-189312.wav",5,10)


# In[ ]:




