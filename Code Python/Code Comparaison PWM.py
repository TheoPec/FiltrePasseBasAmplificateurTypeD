import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

f_sin = 10    
A_sin = 1.0      
f_tri = 200
A_tri = 1.2      
T_obs = 1       
fs = 1000     
t = np.arange(0, T_obs, 1/fs)

sinus = A_sin * np.sin(2 * np.pi * f_sin * t)
tri = A_tri * (2 * np.abs(2 * ((t * f_tri) % 1) - 1) - 1)
pwm = (sinus > tri).astype(float)
amplifiedpwm = 100 * pwm

plt.figure(figsize=(12, 8))
plt.subplot(5, 1, 1)
plt.plot(t, sinus, label='Sinusoïde')
plt.ylabel('Amplitude [V]')
plt.legend()
plt.grid(True)

plt.subplot(5, 1, 2)
plt.plot(t, tri, color='orange', label='Onde triangulaire')
plt.ylabel('Amplitude [V]')
plt.legend()
plt.grid(True)

plt.subplot(5, 1, 3)
plt.plot(t, pwm, color='green', label='PWM (sinus > triangle)')
plt.ylabel('PWM')
plt.xlabel('Temps [s]')
plt.legend()
plt.grid(True)

plt.subplot(5, 1, 4)
plt.plot(t, amplifiedpwm, color='green', label='PWM amplifié')
plt.ylabel('PWM')
plt.xlabel('Temps [s]')
plt.legend()
plt.grid(True)

w, h = freqz(amplifiedpwm, 1, 2**13)
print(w)
plt.subplot(5, 1, 5)
plt.plot(w, 20 * np.log10(np.abs(h)))
plt.title('Réponse fréquentielle de amplifiedpwm')
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Amplitude [dB]')
plt.grid(True)







plt.tight_layout()
plt.show()
