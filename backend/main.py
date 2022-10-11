from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json
import random

import tts.tts as tts
import answers

def whishMe():
    tts.speak("Bom dia!")

whishMe()

# TTS - Text to Speech
#text = "Olá, meu nome é Istáius. No que posso te ajudar?"
#tts.speak(text)

# ASR - Automated Speech Recognition 
model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

WAKEUP = ["pedro", "pietro", "pedra"]

def listen():
    while True:
        data = stream.read(2048)

        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)

            if result is not None:
                text = result['text']
                return text

while True:
    print("Escutando...")
    text = listen()

    for item in WAKEUP:
        if text.count(item) > 0:
            tts.speak(random.choice(answers.TAKECOMMAND))
            text = listen()
            print(text)
            tts.speak(text)