import asyncio
from machine import Pin, DAC, Timer


class AudioPlayerByTimer:
    def __init__(self, pin_num=25, timer_num=0):
        self.timer = Timer(timer_num)
        self.dac = DAC(Pin(pin_num))
        self.buffer = None
        self.buffer_end = 0
        self.pos = 0
        self.ended = True

    def _callback_func(self, t):
        if self.pos >= self.buffer_end:
            self.timer.deinit()
            self.pos = 0
            self.ended = True
        else:
            self.dac.write(self.buffer[self.pos])
            self.pos += 1

    def play(self, buffer, buffer_end, sample_rate=4410):
        self.buffer = buffer
        self.buffer_end = buffer_end
        self.pos = 0
        self.ended = False
        self.timer.init(
            mode=Timer.PERIODIC, freq=sample_rate, callback=self._callback_func
        )
        while not self.ended:
            pass

    async def async_play(self, buffer, buffer_end, sample_rate=4410):
        self.buffer = buffer
        self.buffer_end = buffer_end
        self.pos = 0
        self.ended = False
        self.timer.init(
            mode=Timer.PERIODIC, freq=sample_rate, callback=self._callback_func
        )
        while not self.ended:
            await asyncio.sleep(0)
