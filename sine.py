import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class SineGenerator:

    def sine_tone(self, freq, sampling_rate = 44100, duration = 1, volume = 1):
        return volume * np.sin(2 * np.pi * np.arange(sampling_rate * duration) * freq / sampling_rate)

    def play_sine_tone(self, freq, sampling_rate = 44100, duration = 1, volume = 1):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sampling_rate,
                output=True)
        samples = (self.sine_tone(freq)).astype(np.float32)

        stream.write(volume*samples)
        stream.stop_stream()
        stream.close()
        p.terminate()

    def plot_sine(self, freq, sampling_rate = 44100, duration = 1, volume = 1):
        x = np.linspace(0, 882, sampling_rate)
        y = volume * np.sin(2 * np.pi * x * freq / sampling_rate)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.set_ylim([-1.1, 1.1])
        plot = a.plot(x,y)

        return f
