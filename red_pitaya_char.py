import numpy as np
import matplotlib.pyplot as plt 
from SNR import SNR 
from SFDR import SFDR
from ENOB import ENOB
from FFT_adc_char import FFT
from SINAD import SINAD

# 30 MHZ signal 

# points = [4*2**10 , 8*2**10 , 16*2**10 , 32*2**10]
# filename_1 = "Fin390MHz_p3dBm_Fs2p048GHz_32768pts.lvm"
# filename_2 = "Fin30MHz_p3dBm_Fs2p048GHz_32768pts.lvm"
noise_level = []
filename = "red_pitaya_fft.txt"
fs = 125e6
# desired_freq = int(input("enter desired freq 30 or 390 (Mhz): "))

# if (desired_freq == 30):
#     filename = filename_2
# else:
#     filename = filename_1    

# freq,mag_fft = FFT(filename,0,32*2**10)
data = []
with open(filename, "r") as f:
        data = np.array([float(line.strip()) for line in f]) #line strip removes /n(newline) in file , return as float

half = len(data)//2

mag_power = data/(len(data)*4)        
freq = np.fft.fftfreq(len(data), d = 1/fs)
freq = np.fft.fftshift(freq)
mag_power = mag_power[half:]
freq = freq[half:]
eps = 1e-6
mag_power_db = 10*np.log10((mag_power/np.max(mag_power))+eps)

plt.figure()
plt.plot(freq,mag_power)
plt.xlabel("freq")
plt.ylabel("power")
plt.title("FFT for 1 set of 8k")
plt.grid(True)
plt.show()


plt.figure()
plt.plot(freq,mag_power_db)
plt.xlabel("freq")
plt.ylabel("db")
plt.title("FFT for 1 set of 8k")
plt.grid(True)
plt.show()

start,stop = map(float, input("Enter signal freq range (in Hz, e.g. 100e6,110e6):\n").split(','))
# start,stop = map(float, input("Enter signal freq range (in Hz, e.g. 100e6,110e6):\n").split(','))

#SNR
SNR_8k = SNR(freq,mag_power,start,stop)
print(f"SNR = {SNR_8k} \n")

# SINAD
SINAD_value_8k,noise_8k,mags_noise_8k = SINAD(freq,mag_power,start,stop)
print(f"SINAD = {SINAD_value_8k} \n")

#ENOB
ENOB_8k = ENOB(SINAD_value_8k)
print(f"ENOB is = {ENOB_8k} \n")

#SFDR
SFDR_8k = SFDR(mag_power)
print(f"SFDR is = {SFDR_8k} \n")



