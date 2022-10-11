from gtts import gTTS
from io import BytesIO
import playsound
import os

tts = gTTS('Olá, meu nome é Istáius. No que posso te ajudar?', lang='pt', tld='com.br')
filename = "abc.mp3"
tts.save(filename)
playsound.playsound(filename)
os.remove(filename)