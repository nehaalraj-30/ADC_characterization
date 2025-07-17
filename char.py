import numpy as np
import matplotlib.pyplot as plt 
from SNR import SNR 
from SFDR import SFDR
from ENOB import ENOB
from FFT_adc_char import FFT
from SINAD import SINAD

points = [4*2**10 , 8*2**10 , 16*2**10 , 32*2**10]
filename_1 = "Fin390MHz_p3dBm_Fs2p048GHz_32768pts.lvm"
filename_2 = "Fin30MHz_p3dBm_Fs2p048GHz_32768pts.lvm"
noise_level = []

desired_freq = int(input("enter desired freq 30 or 390 (Mhz): "))

if (desired_freq == 30):
    filename = filename_2
else:
    filename = filename_1    

freq,mag_fft = FFT(filename,0,32*2**10)
eps = 1e-6
mag_db = 20*np.log10(((mag_fft)/np.max(mag_fft))+eps)

plt.plot(freq,mag_db)
plt.xlabel("freq")
plt.ylabel("db")
plt.title("FFT")
plt.grid(True)
plt.show()

start,stop = map(float, input("Enter signal freq range (in Hz, e.g. 100e6,110e6):\n").split(','))

for point in points:
    freq,mag_fft = FFT(filename,0,point)
    eps = 1e-6
    mag_power = mag_fft**2
    SINAD_value,noise,mags_noise = SINAD(freq,mag_power,start,stop)
    noise_level.append(noise)

noise_level_db_fs= 10*np.log10(noise_level)
plt.figure()
plt.plot(points, noise_level_db_fs, marker='o')
plt.xscale("log", base=2)
plt.xlabel("FFT Points (N)")
plt.ylabel("Total Noise Power")
plt.title("Noise Power vs FFT Size")
plt.grid(True, which='both', ls='--')
plt.tight_layout()
plt.show()  

#8k points is the best tradeoff for low fft noise bar and high resolution
point_1 = 0
point_2 = 8*2**10
mag_fft_acc = np.zeros(4*2**10)
mag_power_acc = np.zeros(4*2**10)
#accumalating
for i in range(4):
    freq_8k,mag_fft_8k = FFT(filename,point_1,point_2)
    point_1 = point_2
    point_2 = 8*2**10 + point_2
    mag_power_8k = mag_fft_8k**2
    mag_fft_acc += mag_fft_8k 
    mag_power_acc += mag_power_8k 

mag_power_acc = mag_power_acc/4
mag_fft_acc = mag_fft_acc/4
mag_acc_db = 20*np.log10((mag_fft_acc/np.max(mag_fft_acc))+eps)

freq_8k_1,mag_8k = FFT(filename,0,8*2**10)
eps = 1e-6
mag_db_8k = 20*np.log10(((mag_8k)/np.max(mag_8k))+eps)

plt.figure()
plt.subplot(2,1,1)
plt.plot(freq_8k_1,mag_db_8k)
plt.xlabel("freq")
plt.ylabel("db")
plt.title("FFT for 1 set of 8k")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(freq_8k,mag_acc_db)
plt.xlabel("Frequency(Hz)")
plt.ylabel("db")
plt.title("FFT output for accumaletd 8k")
plt.grid(True)
plt.tight_layout()
plt.show() 

# start,stop = map(float, input("Enter signal freq range (in Hz, e.g. 100e6,110e6):\n").split(','))

#SNR
SNR_8k = SNR(freq_8k,mag_power_acc,start,stop)
print(f"SNR = {SNR_8k} \n")

# SINAD
SINAD_value_8k,noise_8k,signal_8k = SINAD(freq_8k,mag_power_acc,start,stop)
print(f"SINAD = {SINAD_value_8k} \n")


#ENOB
ENOB_8k = ENOB(SINAD_value_8k)
print(f"ENOB is = {ENOB_8k} \n")

#SFDR
SFDR_8k = SFDR(mag_power_acc)
print(f"SFDR is = {SFDR_8k} \n")



