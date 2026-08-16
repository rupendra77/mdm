import numpy as np
import matplotlib.pyplot as plt

# Frequencies
fm = 4
fs = 8

# Time values
t = np.linspace(0, 2, 400)

# Original Signal
signal = np.sin(2 * np.pi * fm * t)

# Sampling Pulse
pulse = (((t * fs) % 1) < 0.2).astype(int)

# Sampled Points
ts = np.linspace(0, 2, fs*2 + 1)
sample = np.sin(2 * np.pi * fm * ts)

# Recovered Signal
recover = np.interp(t, ts, sample)

# Plotting
plt.figure(figsize=(8,8))

plt.subplot(4,1,1)
plt.plot(t, signal)
plt.title("Original Signal")
plt.grid()

plt.subplot(4,1,2)
plt.plot(t, pulse)
plt.title("Sampling Pulse")
plt.grid()

plt.subplot(4,1,3)
plt.stem(ts, sample)
plt.title("Sampled Signal")
plt.grid()

plt.subplot(4,1,4)
plt.plot(t, recover)
plt.title("Recovered Signal")
plt.grid()

plt.tight_layout()
for i in range(1,5):
    plt.subplot(4,1,i)
    plt.xticks(np.arange(0, 2.1, 0.5))
plt.show()