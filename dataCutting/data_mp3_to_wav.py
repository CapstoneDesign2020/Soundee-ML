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


# In[100]:


#5초마다 자르기
def cuttingBasedOnTime5s(wav,file_id):
        length=wav.duration_seconds #오디오 길이
        # print(file_id+str(length))
        # print()
        t1=0*1000
        t2=5*1000
        while length >=5:
            cut_wav=original[t1:t2]
            cut_wav.export('cut0'+'_'+str(t1/1000)+'_'+file_id,format="wav")
            length=length-5
            t1+=5*1000
            t2+=5*1000


# In[102]:


file_list_youtube_wav =glob.glob('dataCutting/baby_crying/wav/*')
print(file_list_youtube_wav)

for wav_file in file_list_youtube_wav:
    if wav_file.endswith('.wav') :
        wav = AudioSegment.from_wav(wav_file)
        file_id=os.path.basename(wav_file)
        cuttingBasedOnTime5s(wav,file_id)


# In[103]:


file_list_dog =glob.glob('dataCutting/dog/*')
print(file_list_dog)

for wav_file in file_list_dog:
    if wav_file.endswith('.wav') :
        file_id=os.path.basename(wav_file)
        wav = AudioSegment.from_wav(wav_file)
        length=wav.duration_seconds #오디오 길이
        if(length>=5) :
            cuttingBasedOnTime5s(wav,file_id)
        else :
            addSilenceWav(wav,length,file_id)
            


# In[104]:


#silence sound 불러오기
silence05=AudioSegment.from_wav('dataCutting/silence/5_silence.wav')
silence04=AudioSegment.from_wav('dataCutting/silence/4_silence.wav')
silence03=AudioSegment.from_wav('dataCutting/silence/3_silence.wav')
silence02=AudioSegment.from_wav('dataCutting/silence/2_silence.wav')
silence01=AudioSegment.from_wav('dataCutting/silence/1_silence.wav')

#공백 추가 하고 5초로 wav file추출하는 함수
def addSilenceWav(wav1,length,file_id):
    # print("addSlice")
    # print(length)
    if length<=1:
        add_silence_wav=wav1+silence05
    elif length <=2 :
        add_silence_wav=wav1+silence04
    elif length <=3 :
        add_silence_wav=wav1+silence03
    elif length <=4:
        add_silence_wav=wav1+silence02
    elif length <=5:
        add_silence_wav=wav1+silence01
            
    t1=0*1000
    t2=5*1000
    add_silence_wav=add_silence_wav[t1:t2]
    add_silence_wav.export('add_silence'+file_id,format="wav")


# In[ ]:




