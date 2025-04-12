import time
import simpleaudio
from usamtts import Reciter, Processor, Renderer
from iter_segments import iter_by_punctuations


reciter = Reciter()
processor = Processor()
renderer = Renderer()


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
        play_obj = simpleaudio.play_buffer(
            renderer.buffer[: renderer.buffer_end],
            1,
            1,
            22050,
        )
        while play_obj.is_playing():
            pass


def main():
    while True:
        play("Hello. My name is Sam. How are you?")
        time.sleep(2)


if __name__ == "__main__":
    main()
