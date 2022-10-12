import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()
speech_config = speechsdk.SpeechConfig(subscription=os.getenv('SPEECH_KEY'), region=os.getenv('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='pt-BR-AntonioNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

def speak(text):
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()