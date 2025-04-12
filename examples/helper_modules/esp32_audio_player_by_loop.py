import time
from machine import Pin, DAC


class AudioPlayerByLoop:
    def __init__(self, pin_num=25):
        self.dac = DAC(Pin(pin_num))
        self.buffer = None
        self.buffer_end = 0
        self.pos = 0
        self.ended = True

    def play(self, buffer, buffer_end, sample_rate=4410):
        self.buffer = buffer
        self.buffer_end = buffer_end
        self.pos = 0
        self.ended = False
        interval_us = 1000000 // sample_rate
        start = time.ticks_us()
        while not self.ended:
            if time.ticks_diff(time.ticks_us(), start) > interval_us:
                start = time.ticks_us()
                if self.pos >= self.buffer_end:
                    self.pos = 0
                    self.ended = True
                    break
                else:
                    self.dac.write(self.buffer[self.pos])
                    self.pos += 1
