import numpy as np 
import matplotlib.pyplot as plt 

# DAC Parametreleri 
bits = 4 
v_ref = 5.0 
lsb = v_ref / (2**bits) 

# İdeal Basamaklar ve Değerler
states = np.arange(16) 
v_ideal = states * lsb 

# R-2R Merdiven Tipi Simülasyon Çıktıları
v_sim = np.array([0.00106, 0.3138, 0.6264, 0.9390, 1.2500, 1.5600, 
                  1.8800, 2.1900, 2.5000, 2.8131, 3.1300, 3.4400, 
                  3.7500, 4.0600, 4.3800, 4.6900]) 

# INL Hesabı (LSB Cinsinden)
inl = (v_sim - v_ideal) / lsb 

# DNL Hesabı (Ardışık basamak farklarının ideal LSB'den sapması)
step_differences = np.diff(v_sim)
dnl = (step_differences - lsb) / lsb 

print(f"Max INL: {np.max(np.abs(inl)):.4f} LSB") 
print(f"Max DNL: {np.max(np.abs(dnl)):.4f} LSB")