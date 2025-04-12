import machine

machine.freq(240000000)

import time
from machine import Pin, DAC
from usamtts import Reciter, Processor, Renderer, time_table
from iter_segments import iter_by_punctuations


class Renderer4410HzAudioPlayer(Renderer):
    def __init__(self, *args, volume=16, **kwargs):
        super().__init__(*args, buffer_size=0, **kwargs)
        self.dac = DAC(Pin(25))
        self.audio_interval_us = 1000000 // 4410
        self.audio_start = time.ticks_us()
        self.play_pos = 0
        self.volume = volume

    def _output(self, index, a):
        self.buffer_pos += time_table[self.old_time_table_index][index]
        self.old_time_table_index = index

        temp_play_pos = self.buffer_pos // 250
        if self.play_pos != temp_play_pos:
            self.play_pos = temp_play_pos
            while True:
                if (
                    time.ticks_diff(time.ticks_us(), self.audio_start)
                    > self.audio_interval_us
                ):
                    self.audio_start = time.ticks_us()
                    self.dac.write((a & 15) * self.volume)
                    break


reciter = Reciter()
processor = Processor()
renderer = Renderer4410HzAudioPlayer(volume=16)


def play(
    paragraph,
    phonetic=False,
    reciter=reciter,
    processor=processor,
    renderer=renderer,
    iter_segments=iter_by_punctuations,
):
    for item in iter_segments(paragraph):
        phonemes = item if phonetic else reciter.text_to_phonemes(item)
        processor.process(phonemes)
        renderer.render(processor)


def main():
    while True:
        play("Hello. My name is Sam. How are you?")
        time.sleep(2)


if __name__ == "__main__":
    main()
