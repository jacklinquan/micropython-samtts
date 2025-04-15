# MicroPython SAMTTS

A Python port of Software Automatic Mouth Test-To-Speech program.

- Ported by: Quan Lin
- License: None

[Try `usamtts` in browser.](https://jacklinquan.github.io/micropython-samtts/)

***WARNING***:
This project is not under any open source software license.
Use it at your own risk.

This MicroPython module `usamtts` is trimmed and optimized for MicroPython from the CPython package
[samtts](https://github.com/jacklinquan/samtts). It keeps the core of `samtts` which consists of
`Reciter`, `Processor` and `Renderer`.
And it puts all the code in a single file for easy installation.
The
[API Reference](https://jacklinquan.github.io/samtts/api)
of these 3 classes is mostly the same as `samtts`.
The difference is that the module name is `usamtts` instead of `samtts`.

---

## What is SAM?

SAM is the Text-To-Speech (TTS) software SAM (Software Automatic Mouth) for the Commodore C64
published in the year 1982 by Don't Ask Software (now SoftVoice, Inc.).

This project is an unofficial Python port of SAM. It is translated by hand from the adaption to C by
[Stefan Macke](https://github.com/s-macke/SAM)
and the refactorings by 
[Vidar Hokstad](https://github.com/vidarh/SAM).

---

## Installation

The Python file `usamtts.py` can be installed on target hardware with `mpremote`:
```shell
pip install mpremote
mpremote mip install github:jacklinquan/micropython-samtts
```

Although the Python file `usamtts.py` can be used directly,
there are massive `bytes` literals in it which will take a lot of RAM.
The best approach is to download it and pre-compile it into bytecode with `mpy-cross`.

```shell
pip install mpy-cross
mpy-cross usamtts.py
```

And then load the generated `usamtts.mpy` to target hardware before using it.

---

## Usage

This module can be used in several different ways to meet different needs.

The core of `usamtts` (`Reciter`, `Processor` and `Renderer`)
can only process very short inputs.
To work around this, long paragraphs can be split into small segments.
I wrote some simple generator functions to help on this.
They are in `iter_segments.py` in
[helper_modules](/examples/helper_modules)
directory.
You can write your own `iter_segments` functions to meet your needs.

### For platforms with abundant RAM

By default the `Renderer` object will render audio data in an internal buffer.
The default configuration of the audio data:
- Sample rate: 22050 Hz (sample interval about 45us)
- Number of channels: 1 (mono)
- Bits per sample: unsigned 8 bits (1 byte per sample)
- Buffer size: 220500 bytes (10 seconds of 22050 Hz audio data)

These requirements are quite demanding for most MicroPython devices.
In case your platform meets all of them, here is an example on how to use it.

<details><summary>Example Code</summary>

```python
import time
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
        audio_data = renderer.buffer[: renderer.buffer_end]
        # Your code to play the audio data starts here
        # `audio_data` is a 22050 Hz, 1 channel, 1 byte per sample audio buffer
        # You may feed it into an I2S device or play it with DAC through a loop (45us interval).
        # You may need to convert the data from unsigned 8 bits to signed 16 bits
        # for I2S devices.

def main():
    while True:
        play("Hello. My name is Sam. How are you?")
        time.sleep(2)

if __name__ == "__main__":
    main()
```
</details>

- Pros:
  - Use `usamtts` as it is. No customization is needed.
  - Full control on the audio data buffer of 22050 Hz.
    You may further process the audio data like filtering and interpolating.
- Cons:
  - It needs plenty of RAM.
  - Response is slow.

### For ESP32 Generic Board

The RAM of ESP32 Generic Board is very limited.
It is impossible to use `usamtts` in the default way.
Given the sound quality of the original SAM,
22050 Hz actually overkills.
The sample rate is reduced to 4410 Hz, and it is still acceptable to me.
For the following examples for ESP32 Generic Board,
the audio data configuration is:
- Sample rate: 4410 Hz (sample interval about 226us)
- Number of channels: 1 (Mono)
- Bits per sample: unsigned 8 bits (1 byte per sample)
- Buffer size: 22050 bytes (5 seconds of 4410 Hz audio data)

To achieve this, we have to subclass `Renderer` class.

With 4410 Hz sample rate, we can play the audio data by loop or timer.
I wrote an `AudioPlayerByLoop` class in `esp32_audio_player_by_loop.py`
and an `AudioPlayerByTimer` class in `esp32_audio_player_by_timer.py` in
[helper_modules](/examples/helper_modules)
directory.

#### Hardware

To check if the concept works,
the hardware can be as simple as ESP32 DevKitC with a passive buzzer.
Just be aware that with a passive buzzer, the volume would be very low.

![esp32_with_buzzer](/pictures/esp32_with_buzzer.jpg)

When you feel confident with the concept,
you may try to replace the buzzer with a speaker.
**Please be aware that it is going to be very loud without volume control!**
One of the examples below shows how to control the volume.

![esp32_with_speaker](/pictures/esp32_with_speaker.jpg)

The examples below are tested with MicroPython v1.24.1 on ESP32 DevKitC.

#### Play audio by loop

<details><summary>Example Code</summary>

```python
import machine

# Make the most of ESP32 CPU.
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
# Instantiate `Renderer4410Hz` as early as possible,
# because it requires large buffer.
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
```
</details>

- Pros:
  - Fairly simple implementation.
  - Audio data of 4410 Hz is stored for further processing.
- Cons:
  - It still takes a lot of RAM for buffering audio data.
  - Response is still not fast.

#### Play audio by timer

<details><summary>Example Code</summary>

```python
import machine

# Make the most of ESP32 CPU.
machine.freq(240000000)

import time
from usamtts import Reciter, Processor, Renderer, time_table
from esp32_audio_player_by_timer import AudioPlayerByTimer
from iter_segments import iter_by_punctuations

class Renderer4410Hz(Renderer):
    def _output(self, index, a):
        self.buffer_pos += time_table[self.old_time_table_index][index]
        self.old_time_table_index = index

        self.buffer_end = self.buffer_pos // 250
        self.buffer[self.buffer_end] = (a & 15) * 16

reciter = Reciter()
processor = Processor()
# Instantiate `Renderer4410Hz` as early as possible,
# because it requires large buffer.
renderer = Renderer4410Hz(buffer_size=22050)

player = AudioPlayerByTimer()

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
```
</details>

- Pros:
  - Fairly simple implementation.
  - Audio data of 4410 Hz is stored for further processing.
- Cons:
  - It still takes a lot of RAM for buffering audio data.
  - Response is still not fast.

#### Play audio by timer asynchronously

ESP32 timers naturally run asynchronously.
An audio player run by timer can work with `asyncio` to run asynchronously.

<details><summary>Example Code</summary>

```python
import machine

# Make the most of ESP32 CPU.
machine.freq(240000000)

import asyncio
from usamtts import Reciter, Processor, Renderer, time_table
from esp32_audio_player_by_timer import AudioPlayerByTimer
from iter_segments import iter_by_punctuations

class Renderer4410Hz(Renderer):
    def _output(self, index, a):
        self.buffer_pos += time_table[self.old_time_table_index][index]
        self.old_time_table_index = index

        self.buffer_end = self.buffer_pos // 250
        self.buffer[self.buffer_end] = (a & 15) * 16

reciter = Reciter()
processor = Processor()
# Instantiate `Renderer4410Hz` as early as possible,
# because it requires large buffer.
renderer = Renderer4410Hz(buffer_size=22050)

player = AudioPlayerByTimer()

async def async_play(
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
        await player.async_play(renderer.buffer, renderer.buffer_end)

async def async_main():
    while True:
        await async_play("Hello. My name is Sam. How are you?")
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(async_main())
```
</details>

- Pros:
  - It works with `asyncio` for asynchronous code.
  - Audio data of 4410 Hz is stored for further processing.
- Cons:
  - It still takes a lot of RAM for buffering audio data.
  - Response is still not fast.

#### Play audio by renderer with volume control (recommended)

<details open><summary>Example Code</summary>

```python
import machine

# Make the most of ESP32 CPU.
machine.freq(240000000)

import time
from machine import Pin, DAC
from usamtts import Reciter, Processor, Renderer, time_table
from iter_segments import iter_by_punctuations

class Renderer4410HzAudioPlayer(Renderer):
    def __init__(self, *args, volume=16, **kwargs):
        # Internal buffer is not needed any more, set its size to 0.
        super().__init__(*args, buffer_size=0, **kwargs)
        self.dac = DAC(Pin(25))
        self.audio_interval_us = 1000000 // 4410
        self.audio_start = time.ticks_us()
        self.play_pos = 0
        # Volume should be in range 0~16.
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
# Set desired volume (maximum 16).
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
        # Audio is played by renderer.
        renderer.render(processor)

def main():
    while True:
        play("Hello. My name is Sam. How are you?")
        time.sleep(2)

if __name__ == "__main__":
    main()
```
</details>

- Pros:
  - It takes the least RAM.
  - Response is very fast.
  - Volume is controllable.
- Cons:
  - More complicated implementation.
  - Audio data is not stored.
    It can not be used for further processing.

### For CPython

`usamtts` is a pure Python module,
and it does not depend on any other library (not even any built-in library).
So, it can be used with CPython as well.
But to play audio, you need to install an audio player that works on your platform.
The following code is tested on Windows.

<details><summary>Example Code</summary>

```python
import time
# pip install simpleaudio
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
```
</details>

### For Brython

As a pure Python module, `usamtts` can also work with
[Brython](https://github.com/brython-dev/brython)
in a browser.
Please try this
[demo](https://jacklinquan.github.io/micropython-samtts/).

Please note that up to Brython v3.13.1 there is a bug on `bytes` literal.
The `usamtts` module used for the demo is modified to work around this bug in Brython.

---

## Useful information

### Phonemes

```text
                 Phoneme Information

     VOWELS                             VOICED CONSONANTS
IY           f(ee)t                     R        red
IH           p(i)n                      L        allow
EH           beg                        W        away
AE           Sam                        W        whale
AA           pot                        Y        you
AH           b(u)dget                   M        Sam
AO           t(al)k                     N        man
OH           cone                       NX       so(ng)
UH           book                       B        bad
UX           l(oo)t                     D        dog
ER           bird                       G        again
AX           gall(o)n                   J        judge
IX           dig(i)t                    Z        zoo
                                        ZH       plea(s)ure
   DIPHTHONGS                           V        seven
EY           m(a)de                     DH       (th)en
AY           h(igh)
OY           boy
AW           h(ow)                      UNVOICED CONSONANTS
OW           slow                       S         Sam
UW           crew                       Sh        fish
                                        F         fish
                                        TH        thin
 SPECIAL PHONEMES                       P         poke
UL           sett(le) (=AXL)            T         talk
UM           astron(omy) (=AXM)         K         cake
UN           functi(on) (=AXN)          CH        speech
Q            kitt-en (glottal stop)     /H        a(h)ead
```

### Pitches

```text
                  Pitch Information

PITCH   NOTE    |   PITCH   NOTE    |   PITCH   NOTE
 104     C1     |     52     C2     |     26     C3
  92     D1     |     46     D2     |     23     D3
  82     E1     |     41     E2     |     21     E3
  78     F1     |     39     F2     |     19     F3
  68     G1     |     34     G2     |     17     G3
  62     A1     |     31     A2     |
  55     B1     |     28     B2     |
```

### Characters

```text
DESCRIPTION         SPEED   PITCH   MOUTH   THROAT
Elf                  72      64      160     110
Little Robot         92      60      190     190
Stuffy Guy           82      72      105     110
Little Old Lady      82      32      145     145
Extra-Terrestrial   100      64      200     150
SAM                  72      64      128     128
```

---

## Limitations

- SAM was developed more than 40 years ago.
  It was advanced in 1980s.
  But now its sound quality is not comparable to AI based TTS programs.
- The core of SAM can only process very short inputs.
  To work around this, long inputs must be split.
- SAM does not pronouce all the words correctly.
  To work around this, phonemes can be used directly.
  But make sure the phonemes are valid, otherwise it will raise exceptions.

---

## Further development

This project is meant to be a fairly faithful port of the original SAM.
It will not improve upon SAM in any manner,
like improving the quality of the sound or
breaking the limitations of SAM.

The further development of this project is limited to bug fixing.
If anyone is interested in improving it,
please fork it and start a new project.

---

## About license

According to
[Stefan Macke](https://github.com/jacklinquan/samtts/blob/main/Stefan_Macke_SAM_README.md)
and
[Vidar Hokstad](https://github.com/jacklinquan/samtts/blob/main/Vidar_Hokstad_SAM_README.md)
the status of the original software can be best described as
[Abandonware](https://en.wikipedia.org/wiki/Abandonware).

Neither Stefan Macke nor Vidar Hokstad put their projects under any open source software license.
As long this is the case I cannot put my code under any open source software license either.
However the software might be used under the
["Fair Use" act](https://en.wikipedia.org/wiki/FAIR_USE_Act)
in the USA.
In fact,
[The MicroPython port for BBC micro:bit](https://github.com/bbcmicrobit/micropython)
has been using
[SAM in C by Stefan Macke](https://github.com/s-macke/SAM)
as the core of its `speech` module for many years.
