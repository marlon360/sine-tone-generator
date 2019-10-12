import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class SinusGenerator:

    def sinus_tone(self, freq, sampling_rate = 44100, duration = 1, volume = 1):
        return volume * np.sin(2 * np.pi * np.arange(sampling_rate * duration) * freq / sampling_rate)

    def play_sinus_tone(self, freq, sampling_rate = 44100, duration = 1, volume = 1):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sampling_rate,
                output=True)
        samples = (self.sinus_tone(freq)).astype(np.float32)

        stream.write(volume*samples)
        stream.stop_stream()
        stream.close()
        p.terminate()

    def plot_sinus(self, freq, sampling_rate = 44100, duration = 1, volume = 1):
        x = np.linspace(0, 882, sampling_rate)
        y = volume * np.sin(2 * np.pi * x * freq / sampling_rate)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.set_ylim([-1.1, 1.1])
        plot = a.plot(x,y)

        return f



# generate samples, note conversion to float32 array
#samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]


# play. May repeat with different volume values (if done interactively)



# plot_sinus(440.0)

