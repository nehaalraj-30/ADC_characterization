# ADC_characterization

This is a Python script to help you analyze the performance of the ADC (Analog-to-Digital Converter) on the ZCU111 board, using raw data files. It calculates and shows important ADC quality metrics like SNR, SINAD, ENOB, and SFDR.
 
Requirements: 


The following helper Python files in your folder:

    SNR.py

    SFDR.py

    ENOB.py

    FFT_adc_char.py

    SINAD.py

ADC data files in .lvm format (for example, the script expects files like Fin390MHz_p3dBm_Fs2p048GHz_32768pts.lvm)

Function


    Loads raw data from your chosen file.

    Performs FFT and plots the signal spectrum.

    Measures noise levels at different FFT sizes.

    Averages multiple FFT segments to improve results.

    Calculates key ADC performance numbers and shows them.


