import random
import pretty_midi

class MidiMusician:

    T             = 0.0
    BEATS_PER_MIN = 120.0
    QUARTER       = 60 / BEATS_PER_MIN
    WHOLE         = QUARTER * 4
    HALF          = QUARTER * 2
    QUARTER_TRIP  = WHOLE / 6
    EIGHTH        = WHOLE / 8
    EIGHTH_TRIP   = WHOLE / 12
    SIXTEENTH     = WHOLE / 16
    THIRTYSECOND  = WHOLE / 32.0

    NOTE_LENGTHS  = [WHOLE, HALF, QUARTER_TRIP, QUARTER, EIGHTH_TRIP, EIGHTH, SIXTEENTH, THIRTYSECOND]

    C1 = 24
    C2 = 36
    C3 = 48
    C4 = 60
    C5 = 72
    C6 = 84
    C7 = 96
    C8 = 108

    INSTRUMENTS = []

    def __init__(self):
        self.pm = pretty_midi.PrettyMIDI(initial_tempo=self.BEATS_PER_MIN)
  
    def add_instrument(self, instrument):
        self.pm.instruments.append(pretty_midi.Instrument(instrument))
        self.INSTRUMENTS.append(instrument)

    def write_file(self, filename):
        self.pm.write(filename)

    def play_note(self, instrument, note, duration, velocity, addTime=True):
        self.pm.instruments[instrument].notes.append(
            pretty_midi.Note(velocity, note, self.T, self.T + duration))
        if addTime:
            self.T += duration

    def play_notes_even(self, instrument, notes, duration, velocity, addTime=True):
        startTime = self.T
        for note in notes:
            self.play_note(instrument, note, duration, velocity, True)
        if addTime == False: 
            self.T = startTime 

    def play_notes_variable(self, instrument, notes, durations, velocity, addTime=True):
        startTime = self.T
        for note, duration in zip(notes, durations):
            self.play_note(instrument, note, duration, velocity, True)
        if addTime == False: 
            self.T = startTime 

    def play_chord(self, instrument, notes, duration, velocity, addTime=True):
        for note in notes:
            self.pm.instruments[instrument].notes.append(
                pretty_midi.Note(velocity, note, self.T, self.T + duration))
        if addTime:
            self.T += duration

    def play_rest(self, duration):
        self.T += duration

    def major_scale(self, note, bounded=False):
        scale = [note, note + 2, note + 4, note + 5, note + 7, note + 9, note + 11]
        if bounded:
            scale.append(note + 12)
        return scale

    def dominant_scale(self, note, bounded=False):
        scale = [note, note + 2, note + 4, note + 5, note + 7, note + 9, note + 10]
        if bounded:
            scale.append(note + 12)
        return scale

    def minor_scale(self, note, bounded=False):
        scale = [note, note + 2, note + 3, note + 5, note + 7, note + 9, note + 10]
        if bounded:
            scale.append(note + 12)
        return scale

    def major_triad(self, note):
        return [note, note + 4, note + 7]

    def minor_triad(self, note):
        return [note, note + 3, note + 7]

    def fourth_stack(self, note, length):
        stack = [note]  
        for i in range(length - 1):
            stack.append(stack[i] + 5)
        return stack

    def fifth_stack(self, note, length):
        stack = [note]
        for i in range(length - 1):
            stack.append(stack[i] + 7)
        return stack

    def gen_notes(self, scale, length):
        return [random.choice(scale) for i in range(length)]

    def gen_times(self, length):
        return [random.choice(self.NOTE_LENGTHS) for i in range(length)]

