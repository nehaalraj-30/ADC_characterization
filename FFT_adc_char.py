import numpy as np

def FFT(filename,point_1,point_2):
    fs = 2.048e9
    data = []
    
    with open(filename, "r") as f:
        data = np.array([float(line.strip()) for line in f]) #line strip removes /n(newline) in file depends on file 

    
    data = data[point_1:point_2]    

    fft = np.fft.fft(data)/len(data)
    fft_shift = np.fft.fftshift(fft)
    mag_fft = np.abs(fft_shift)
    freq = np.fft.fftfreq(len(data), d=1/fs)
    freq = np.fft.fftshift(freq)

    #taking positive freq
    half = len(freq) // 2
    freq = freq[half:]
    mag_fft = mag_fft[half:]
    
    return freq, mag_fft
