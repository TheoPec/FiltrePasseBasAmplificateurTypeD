import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import buttord, butter, freqs


fp = 20_000      
fs = 25_000      
Ap = 1
As = 40         
wp = 2 * np.pi * fp
ws = 2 * np.pi * fs


N, Wn = buttord(wp, ws, Ap, As, analog=True)
print(f"Ordre du filtre Butterworth : {N}")
print(f"Pulsation de coupure normalisée Wn : {Wn:.2e} rad/s")


b, a = butter(N, Wn, btype='low', analog=True)

print("Numérateur b(p) :", b)
print("Dénominateur a(p):", a)


w = np.logspace(2, 6, 2000)
w, h = freqs(b, a, w)


f = w / (2 * np.pi)
H_db = 60 + (20 * np.log10(np.abs(h)))

plt.figure()
plt.semilogx(f, H_db)
plt.axvline(fp, linestyle='--')
plt.axvline(fs, linestyle='--')
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Gain (dB)")
plt.title("Filtre passe-bas Butterworth")
plt.grid(True, which="both", ls=":")
plt.show()
