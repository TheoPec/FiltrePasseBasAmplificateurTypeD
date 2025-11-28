import numpy as np
import matplotlib.pyplot as plt

f_sin = 0.1      
A_sin = 1.0      
f_tri = 2   
A_tri = 1.2      
T_obs = 30       
fs = 1000        
t = np.arange(0, T_obs, 1/fs)

sinus = A_sin * np.sin(2 * np.pi * f_sin * t)
tri = A_tri * (2 * np.abs(2 * ((t * f_tri) % 1) - 1) - 1)
pwm = (sinus > tri).astype(float)

plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, sinus, label='Sinusoïde 0,1 Hz')
plt.ylabel('Amplitude [V]')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, tri, color='orange', label='Onde triangulaire 1 Hz')
plt.ylabel('Amplitude [V]')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, pwm, color='green', label='PWM (sinus > triangle)')
plt.ylabel('PWM')
plt.xlabel('Temps [s]')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
