from browser import document, html, window, timer, alert, console, bind  # type: ignore
import struct
import base64

from usamtts import Reciter, Processor, Renderer


def main():
    def follow_value(a, b):
        a.text = b.value

    def iter_by_punctuations(paragraph):
        head = 0
        tail = head
        while head < len(paragraph):
            while tail < len(paragraph):
                tail += 1
                if tail >= len(paragraph):
                    yield paragraph[head : tail + 1]
                    head = tail + 1
                    tail = head
                    break
                if paragraph[tail] in "!,.:;?":
                    yield paragraph[head : tail + 1]
                    head = tail + 1
                    tail = head

    def play_audio_data(
        audio_data,
        sample_rate=22050,
    ):
        context = window.AudioContext.new({"sampleRate": sample_rate})
        arrayBuffer = context.createBuffer(1, len(audio_data), context.sampleRate)
        nowBuffering = arrayBuffer.getChannelData(0)
        for i in range(len(audio_data)):
            nowBuffering[i] = audio_data[i] / 128 - 1
        source = context.createBufferSource()
        source.buffer = arrayBuffer
        source.connect(context.destination)
        source.start()

    def get_wav_bytes(
        audio_data,
        sample_rate=22050,
    ):
        num_channels = 1
        bits_per_sample = 8
        num_samples = len(audio_data)

        # WAV header fields
        byte_rate = sample_rate * num_channels * bits_per_sample // 8
        block_align = num_channels * bits_per_sample // 8
        data_size = num_samples * block_align
        fmt_chunk_size = 16
        audio_format = 1  # PCM
        chunk_size = 4 + (8 + fmt_chunk_size) + (8 + data_size)

        header = struct.pack(
            "<4sI4s4sIHHIIHH4sI",
            b"RIFF",
            chunk_size,
            b"WAVE",
            b"fmt ",
            fmt_chunk_size,
            audio_format,
            num_channels,
            sample_rate,
            byte_rate,
            block_align,
            bits_per_sample,
            b"data",
            data_size,
        )

        # 8-bit PCM is unsigned, values between 0 and 255
        data = bytes(audio_data)

        return header + data

    def download_wav_file(wav_bytes, file_name="output.wav"):
        b64 = base64.b64encode(wav_bytes).decode("utf-8")
        data_url = f"data:audio/wav;base64,{b64}"

        a = html.A("Download", href=data_url, download=file_name)
        a.style.display = "none"
        document <= a
        a.click()
        a.remove()

    def say(event):
        reciter = Reciter()
        processor = Processor()
        renderer = Renderer(
            speed=int(html_input_speed.value),
            pitch=int(html_input_pitch.value),
            mouth=int(html_input_mouth.value),
            throat=int(html_input_throat.value),
        )

        time_out = 0
        for item in iter_by_punctuations(html_input_text.value):
            phonemes = reciter.text_to_phonemes(item)
            processor.process(phonemes)
            renderer.render(processor)

            timer.set_timeout(
                play_audio_data,
                time_out,
                renderer.buffer[: renderer.buffer_end],
            )
            time_out += renderer.buffer_end * 1000 / 22050 + 100

    def download(event):
        reciter = Reciter()
        processor = Processor()
        renderer = Renderer(
            speed=int(html_input_speed.value),
            pitch=int(html_input_pitch.value),
            mouth=int(html_input_mouth.value),
            throat=int(html_input_throat.value),
        )

        full_audio_data = bytearray()
        for item in iter_by_punctuations(html_input_text.value):
            phonemes = reciter.text_to_phonemes(item)
            processor.process(phonemes)
            renderer.render(processor)
            full_audio_data += renderer.buffer[: renderer.buffer_end]

        wav_bytes = get_wav_bytes(full_audio_data)
        try:
            download_wav_file(wav_bytes)
        except Exception:
            alert("The wav file is too large to generate!")

    # Header
    document <= html.NAV(
        html.DIV(
            html.DIV("USAMTTS", Class="brand-logo center"),
            Class="nav-wrapper container center",
        ),
        Class="teal",
        role="navigation",
    )

    html_input_text = html.INPUT(
        type="text", maxlength="50", value="Hello. My name is Sam. How are you?"
    )
    html_label_speed = html.LABEL("72")
    html_input_speed = html.INPUT(
        type="range", min="0", max="255", value=html_label_speed.text
    )
    html_label_pitch = html.LABEL("64")
    html_input_pitch = html.INPUT(
        type="range", min="0", max="255", value=html_label_pitch.text
    )
    html_label_mouth = html.LABEL("128")
    html_input_mouth = html.INPUT(
        type="range", min="0", max="255", value=html_label_mouth.text
    )
    html_label_throat = html.LABEL("128")
    html_input_throat = html.INPUT(
        type="range", min="0", max="255", value=html_label_throat.text
    )
    html_button_say = html.BUTTON("Say")
    html_button_download = html.BUTTON("Download")

    html_input_speed.bind(
        "input", (lambda ev, a=html_label_speed, b=html_input_speed: follow_value(a, b))
    )
    html_input_pitch.bind(
        "input", (lambda ev, a=html_label_pitch, b=html_input_pitch: follow_value(a, b))
    )
    html_input_mouth.bind(
        "input", (lambda ev, a=html_label_mouth, b=html_input_mouth: follow_value(a, b))
    )
    html_input_throat.bind(
        "input",
        (lambda ev, a=html_label_throat, b=html_input_throat: follow_value(a, b)),
    )

    html_button_say.bind("click", say)
    html_button_download.bind("click", download)

    # Leave some space
    document <= html.P()
    document <= html_input_text
    document <= html.P()
    document <= html.P("Speed ") <= html_label_speed
    document <= html_input_speed
    document <= html.P()
    document <= html.P("Pitch ") <= html_label_pitch
    document <= html_input_pitch
    document <= html.P()
    document <= html.P("Mouth ") <= html_label_mouth
    document <= html_input_mouth
    document <= html.P()
    document <= html.P("Throat ") <= html_label_throat
    document <= html_input_throat
    document <= html.P()
    document <= html_button_say
    document <= html.P()
    document <= html_button_download

    # Must do window.M.AutoInit() after all html being loaded!
    window.M.AutoInit()


if __name__ == "__main__":
    main()
