from tkinter import Tk, Label, Button, Entry, Scale, HORIZONTAL
from sinus import SinusGenerator

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SinusGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sinus Tone")

        self.sin = SinusGenerator()

        self.freq_label = Label(master, text="Frequency:")
        self.freq_label.pack()
        self.freq_scale = Scale(master, from_=50, to=5000, orient=HORIZONTAL)
        self.freq_scale.set(440)
        self.freq_scale.pack()
        
        self.volume_label = Label(master, text="Volume:")
        self.volume_label.pack()
        self.volume_scale = Scale(master, from_=0, to=1,resolution=0.1,  orient=HORIZONTAL)
        self.volume_scale.set(0.5)
        self.volume_scale.pack()

        self.play_button = Button(master, text="Play", command=self.play)
        self.play_button.pack()

        f = self.sin.plot_sinus(440, volume=0.5)
        self.canvas = FigureCanvasTkAgg(f, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


        
    
    def play(self):
        freq = float(self.freq_scale.get())
        vol = float(self.volume_scale.get())
        self.sin.play_sinus_tone(freq, volume=vol)
        self.add_plot()
    
    def add_plot(self):
        freq = float(self.freq_scale.get())
        vol = float(self.volume_scale.get())
        f = self.sin.plot_sinus(freq, volume=vol)
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(f, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
