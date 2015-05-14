from player import MidiPlayer
from musician import MidiMusician

if __name__ == '__main__':
    player = MidiPlayer()
    mm = MidiMusician()
    mm.add_instrument(0)

    mm.play_note(0, mm.C4, 1.0, 100)

    mm.write_file('starter.mid')
    player.play_midi_file('starter.mid')
