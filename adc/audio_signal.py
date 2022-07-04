import math
import numpy as np
from utility import file_handler as fh

def pure_tone(amplitude, frequency, phase, duration, sample_rate):
    n_sample = int(duration * sample_rate)
    af = math.tau * frequency
    vt = np.array(range(n_sample)/float(sample_rate), float)
    return amplitude * np.sin(af * vt + phase / math.tau)
