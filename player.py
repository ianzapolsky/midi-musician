from subprocess import Popen

class MidiPlayer:

    def play_midi_file(self, midi_filename):
        p = Popen(["/Applications/VLC old.app/Contents/MacOS/VLC", "-I", "dummy", midi_filename, "vlc://quit"])
