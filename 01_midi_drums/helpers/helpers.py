from io import StringIO 
import sys

from music21 import stream

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def stream_string(stream: stream.Stream, n_lines: int = 10) -> str:
    """    
    a small hack so we can capture the output of
    music21 and shorten it so our notebook does not
    get spammed.

    uses a context manager from
    https://stackoverflow.com/a/16571630/347577
    """
    with Capturing() as output:
        stream.show('text')

    return '\n'.join(output[0:n_lines])
