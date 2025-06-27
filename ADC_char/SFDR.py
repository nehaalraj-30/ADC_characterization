import numpy as np

def SFDR(mag_power_acc,mags_power_noise):

    mags_power = mag_power_acc
    eps = 1e-6
    mag_power_db = 10*np.log10((mags_power))
    mag_noise_db = 10*np.log10((mags_power_noise))

    SFDR = np.max(mag_power_db) - np.max(mag_noise_db)

    return SFDR