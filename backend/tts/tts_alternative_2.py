import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

engine.say("Olá, meu nome é Istáius. No que posso te ajudar?")
engine.runAndWait()