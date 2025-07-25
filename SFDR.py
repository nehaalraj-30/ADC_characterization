import numpy as np

def SFDR(mag_power_acc):

    mags_power = mag_power_acc
    mags_db = 10*np.log10(mags_power/np.max(mags_power))

    sort_mags_power = sorted(mags_db)

    SFDR = sort_mags_power[-1] - sort_mags_power[-2]

    return SFDR