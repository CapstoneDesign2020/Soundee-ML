def audio_preprocessing():
    import librosa
    import librosa.display
    # import IPython.display
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import matplotlib.font_manager as fm
    import glob
    from IPython import get_ipython


    # get_ipython().run_line_magic('matplotlib', 'inline')

    FIG_SIZE = (15,10)
    

    folder_list = glob.glob("audio_data/*") # 오디오 데이터 파일 위치 
    print(folder_list)
    print(len(folder_list))
    index=0
    for i in folder_list:
        frame_length = 0.025
        frame_stride = 0.010
        y, sr = librosa.load(i,sr=16000)
        win_length = int(np.ceil(frame_length*sr))
        window = 'hamming'
        nfft = int(round(sr*frame_length))
        hop_length = int(round(sr*frame_stride))
        S = librosa.core.stft(y, n_fft=nfft, hop_length=hop_length, win_length=win_length, window=window, center=False)
        Si = librosa.feature.melspectrogram(y=y,sr=sr,S=S, n_mels=40, n_fft=nfft, hop_length=hop_length,win_length=win_length, window=window,center=True, pad_mode='reflect', power=2.0,  fmin=0.0, fmax=sr/2.0)
        DB = librosa.amplitude_to_db(Si, ref=np.max)
        plt.figure(figsize=FIG_SIZE)
        librosa.display.specshow(DB, sr=sr, hop_length=hop_length)
        # plt.xlabel("Time")
        # plt.ylabel("MFCC coefficients")
        # plt.colorbar()
        # plt.title("MFCCs")
        plt.axis('off')
        #save image
        fig = plt.gcf() 
        fig.savefig("./model_image/"+str(index)+'.png',bbox_inches='tight',pad_inches=0)
        # S = librosa.feature.melspectrogram(y=y, n_mels=40, n_fft=input_nfft, hop_length=input_stride)
        
        # n_mels = 40
        # n_fft = int(np.ceil(0.040*sr)) ## I'm not sure how to complete this parameter
        # win_length = int(np.ceil(0.040*sr)) # 0.025*22050
        # hop_length = int(np.ceil(0.020*sr)) #0.010 * 22050
        # window = 'hamming'
        # # 복소공간 값 절댓갑 취해서, magnitude 구하기
        # magnitude = np.abs(fft) 

        # # Frequency 값 만들기
        # f = np.linspace(0,sr[index],len(magnitude))

        # # 푸리에 변환을 통과한 specturm은 대칭구조로 나와서 high frequency 부분 절반을 날려고 앞쪽 절반만 사용한다.
        # left_spectrum = magnitude[:int(len(magnitude)/2)]
        # left_f = f[:int(len(magnitude)/2)]
        # # STFT -> spectrogram
        # hop_length = 512  # 전체 frame 수
        # n_fft = 2048  # frame 하나당 sample 수

        # # calculate duration hop length and window in seconds
        # hop_length_duration = float(hop_length)/sr[index]
        # n_fft_duration = float(n_fft)/sr[index]

        # # STFT
        # stft = librosa.stft(sig[index], n_fft=n_fft, hop_length=hop_length)

        # # 복소공간 값 절댓값 취하기
        # magnitude = np.abs(stft)

        # # magnitude > Decibels 
        # log_spectrogram = librosa.amplitude_to_db(magnitude)
        # # MFCCs
        # # extract 40 MFCCs
        # MFCCs = librosa.feature.mfcc(sig[index], sr[index], n_fft=n_fft, hop_length=hop_length, n_mfcc=40)
        # #display MFCCs
        # plt.figure()
        # librosa.display.specshow(MFCCs, sr=sr[index], hop_length=hop_length)
        # # plt.xlabel("Time")
        # # plt.ylabel("MFCC coefficients")
        # # plt.colorbar()
        # # plt.title("MFCCs")
        # plt.axis('off')
        # #save image
        # fig = plt.gcf() 
        
        

        # fig.savefig("./model_image/"+str(index)+'.png',bbox_inches='tight',pad_inches=0)
        index+=1
    print("complete!")       
