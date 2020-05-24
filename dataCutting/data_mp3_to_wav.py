#!/usr/bin/env python
# coding: utf-8

# In[52]:


from pydub import AudioSegment
import glob
import os


# In[53]:


file_list_youtube =glob.glob('dataCutting/baby_crying/*')
print(file_list_youtube)


# In[59]:


#mp3에서 wav로 변환
def formatFromMp3ToWav(mp3):
    if wav.endswith('.mp3') :
        # 확장자명 제외하고 파일이름 저장
        file_id=os.path.splitext(mp3)
        file_id=os.path.split(file_id[0])
        file_id=file_id[1]
        print(file_id)
        sound = AudioSegment.from_mp3(mp3)
        sound.export(file_id+".wav", format="wav")


# In[60]:


for sound in file_list_youtube:
    formatFromMp3ToWav(sound)


# In[61]:


#5초마다 자르기
def cuttingBasedOnTime5s(wav):
    if wav.endswith('.wav') :
        original = AudioSegment.from_wav(wav)
        length=original.duration_seconds #오디오 길이
        file_id=os.path.basename(wav)
        t1=0*1000
        t2=5*1000
        while length >=5:
            cut_wav=original[t1:t2]
            cut_wav.export('cut0'+'_'+str(t1/1000)+'_'+file_id,format="wav")
            length=length-5
            t1+=5*1000
            t2+=5*1000


# In[62]:


file_list_youtube_wav =glob.glob('dataCutting/baby_crying/wav/*')
print(file_list_youtube_wav)

for wav in file_list_youtube_wav:
    cuttingBasedOnTime5s(wav)

