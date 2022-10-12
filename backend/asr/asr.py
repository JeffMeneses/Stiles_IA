import os
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription=os.getenv('SPEECH_KEY'), region=os.getenv('SPEECH_REGION'))
speech_config.speech_recognition_language="pt-BR"

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

def listen():
    print("Escutando...")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    return speech_recognition_result.text