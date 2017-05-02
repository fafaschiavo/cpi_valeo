#!/usr/bin/python
from scikits.audiolab import wavread
from pylab import *

print 'Hi there'
signal, fs, enc = wavread('track_test.wav')
specgram(signal)
show()