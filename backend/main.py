import random
import datetime

from regex import D

import tts.tts_alternative_2 as tts
import asr.asr as asr
import answers
import IA

def whishMe():
    hour = int(datetime.datetime.now().hour)
    greeting = ""
    if hour>=0 and hour<12:
        greeting = "Bom dia."

    elif hour>=12 and hour<18:
        greeting = "Boa tarde."

    else:
        greeting = "Boa noite."
    tts.speak(greeting+" Eu sou o Istáius, se precisar de algo é só me chamar pelo nome.")

whishMe()

# Temporary function, it'll be removed soon
def executeCommand(intent):
    if intent["goal"] == 'greet':
        tts.speak(random.choice(answers.GREET))
    elif intent["goal"] == 'whoAreYou':
        tts.speak(random.choice(answers.WHOAMI))
    elif intent["goal"] == 'openApp':
        for item in intent["features"]:
            if item["name"] == "appName":
                tts.speak(f"Ok, estou abrindo o aplicativo {item['value']} pra você")

# ASR - Automated Speech Recognition
WAKEUP = ["Stiles", "Stylus", "Stairs"]

while True:
    print("Escutando...")
    text = asr.listen()
    print(text)
    for item in WAKEUP:
        if text.count(item) > 0:
            tts.speak(random.choice(answers.TAKECOMMAND))

            print("Escutando...")
            text = asr.listen()
            print(text)

            intent = IA.evaluateIntent(text)
            executeCommand(intent)
