"""
PyAudio compatibility shim using sounddevice.
"""

import sounddevice as sd
import queue

# --- PyAudio-compatible constants at module level ---
paInt16 = 8  # PyAudio's constant for 16-bit signed integer audio
paInt32 = 1  # 32-bit signed integer audio
paInt8 = 16  # 8-bit signed integer audio
paUInt8 = 32 # 8-bit unsigned integer audio
paFloat32 = 1 # 32-bit float audio


def get_sample_size(format):
    if format == paInt16:
        return 2
    raise ValueError("Unsupported format")


class Stream:
    """A sounddevice-based stream that mimics PyAudio's Stream interface."""

    def __init__(self, rate, channels, format, input, frames_per_buffer, input_device_index=None):
        self.rate = rate
        self.channels = channels
        self.frames_per_buffer = frames_per_buffer
        self._queue = queue.Queue()
        self._stream = None
        self.input_device_index = input_device_index

    def _callback(self, indata, frames, time_info, status):
        self._queue.put(bytes(indata))

    def start(self):
        self._stream = sd.RawInputStream(
            samplerate=self.rate,
            channels=self.channels,
            dtype='int16',
            blocksize=self.frames_per_buffer,
            device=self.input_device_index,
            callback=self._callback,
        )
        self._stream.start()

    def stop(self):
        if self._stream:
            self._stream.stop()

    def stop_stream(self):
        self.stop()

    def is_stopped(self):
        if self._stream:
            return not self._stream.active
        return True

    def close(self):
        if self._stream:
            self._stream.close()
            self._stream = None

    def read(self, num_frames, exception_on_overflow=True):
        return self._queue.get()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()
        self.close()


class PyAudio:
    """Minimal PyAudio-compatible wrapper around sounddevice."""

    # Copy constants into the class attributes as well
    paInt16 = paInt16
    paInt32 = paInt32
    paInt8 = paInt8
    paUInt8 = paUInt8
    paFloat32 = paFloat32

    def __init__(self):
        pass

    def get_device_count(self):
        return len(sd.query_devices())

    def get_device_info_by_index(self, index):
        info = sd.query_devices(index)
        return {
            'index': index,
            'name': info['name'],
            'maxInputChannels': info['max_input_channels'],
            'maxOutputChannels': info['max_output_channels'],
            'defaultSampleRate': info['default_samplerate'],
        }

    def get_default_input_device_info(self):
        idx = sd.default.device[0]
        if idx is None or idx < 0:
            for i, dev in enumerate(sd.query_devices()):
                if dev['max_input_channels'] > 0:
                    idx = i
                    break
        if idx is None or idx < 0:
            raise IOError("No default input device available")
        return self.get_device_info_by_index(idx)

    def open(self, rate=None, channels=None, format=None, input=False,
             frames_per_buffer=1024, input_device_index=None, **kwargs):
        stream = Stream(
            rate=rate,
            channels=channels,
            format=format,
            input=input,
            frames_per_buffer=frames_per_buffer,
            input_device_index=input_device_index,
        )
        stream.start()
        return stream

    def get_sample_size(self, format):
        if format == paInt16:
            return 2
        raise ValueError("Unsupported format")

    def terminate(self):
        pass