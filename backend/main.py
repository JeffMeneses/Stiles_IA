from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json

import tts.tts as tts


# TTS - Text to Speech
#text = "Olá, meu nome é Istáius. No que posso te ajudar?"
#tts.speak(text)

# ASR - Automated Speech Recognition 
model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            print(text)
            tts.speak(text)