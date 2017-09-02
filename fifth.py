from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note
notes1 = NoteSeq([Note(7, dur = .25), Note(7, dur = .25, Note(7, dur = .25), Note(3, dur = 1), Note(5, dur = .25), Note(5, dur = .25), Note(5, dur = .25), Note(2, dur = 1)
midi = Midi(number_tracks = 1, tempo = 108)
midi.seq_notes(notes1,track = 0)
mid.write("fifth10.mid")
