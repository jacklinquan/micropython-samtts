import machine

machine.freq(240000000)

import time
from usamtts import Reciter, Processor, Renderer, time_table
from esp32_audio_player_by_loop import AudioPlayerByLoop
from iter_segments import iter_by_punctuations


class Renderer4410Hz(Renderer):
    def _output(self, index, a):
        self.buffer_pos += time_table[self.old_time_table_index][index]
        self.old_time_table_index = index

        self.buffer_end = self.buffer_pos // 250
        self.buffer[self.buffer_end] = (a & 15) * 16


reciter = Reciter()
processor = Processor()
renderer = Renderer4410Hz(buffer_size=22050)

player = AudioPlayerByLoop()


def play(
    paragraph,
    phonetic=False,
    reciter=reciter,
    processor=processor,
    renderer=renderer,
    player=player,
    iter_segments=iter_by_punctuations,
):
    for item in iter_segments(paragraph):
        phonemes = item if phonetic else reciter.text_to_phonemes(item)
        processor.process(phonemes)
        renderer.render(processor)
        player.play(renderer.buffer, renderer.buffer_end)


def main():
    while True:
        play("Hello. My name is Sam. How are you?")
        time.sleep(2)


if __name__ == "__main__":
    main()
