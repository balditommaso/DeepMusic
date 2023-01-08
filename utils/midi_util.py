from music21 import *
from IPython.display import Image

class MidiUtils:
    
    def __init__(self, path) -> None:
        self.title = path.split('/')[-1]
        self.midi_file = midi.MidiFile()
        self.midi_file.open(path)
        self.midi_file.read()
        self.midi_file.close()
        
    def play_midi(self) -> None:
        s = midi.translate.midiFileToStream(self.midi_file)
        s.show('midi')
    
    def get_title(self) -> None:
        return self.title
    

