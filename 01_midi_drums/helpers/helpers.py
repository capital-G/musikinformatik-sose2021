import os
from typing import Dict
import json

import numpy as np
from mido import KeySignatureError
import pretty_midi as pm
import note_seq


def default(obj):
    if type(obj).__module__ == np.__name__:
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj.item()
    raise TypeError('Unknown type:', type(obj))


def parse_midi_file_async(
    midi_file_path: str,
    proto_save_path: str = '../datasets/lmd/proto/',
    json_save_path: str = '../datasets/lmd/json/',
    save_json: bool = False,
) -> Dict:
    pm.pretty_midi.MAX_TICK = 1e7
    r = {
        'midi_path': midi_file_path,
        'midi_error': True,
    }
    midi_name = os.path.splitext(midi_file_path.split(os.sep)[-1])[0]
    proto_path = os.path.join(proto_save_path, f'{midi_name}.protobuf')
    json_path = os.path.join(json_save_path, f'{midi_name}.json')
    
    try:
        stream = pm.PrettyMIDI(midi_file_path)
        r['midi_error'] = False
    except (OSError, ValueError, IndexError, KeySignatureError, EOFError, ZeroDivisionError):
        return r
    
    try:
        # r['beat_start'] = stream.estimate_beat_start() # omitted b/c adds 200ms to parsing
        r['estimate_tempo'] = stream.estimate_tempo()
        r['tempi_sec'], r['tempi'] = stream.get_tempo_changes() 
        r['end_time'] = stream.get_end_time()
        r['drums'] = any([i.is_drum for i in stream.instruments])
        r['resolution'] = stream.resolution
        r['instrument_names'] = [i.name.strip() for i in stream.instruments]
        r['num_time_signature_changes'] = len(stream.time_signature_changes)
    except ValueError as e:
        # ValueError: Can't estimate beat start when there are no notes.
        # ValueError: Can't provide a global tempo estimate when there are fewer than two notes.
        print(f"Could not parse MIDI file {midi_file_path}: {e}")
    
    try:
        notes = note_seq.midi_to_note_sequence(stream)
    except Exception as e:
        print(f'Could not convert {midi_name} to note sequence')
        return r
    with open(proto_path, 'wb') as f:
        f.write(notes.SerializeToString())
    r['proto_path'] = proto_path
    
    if save_json:
        with open(json_path, 'w') as f:
            json.dump(r, f, default=default)
    
    # free memory
    stream = None
    notes = None
    
    return r
