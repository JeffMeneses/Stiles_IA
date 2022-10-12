import random
import datetime

import tts.tts as tts
import asr.asr as asr
import answers

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
def executeCommand(text):
    if text == 'qual é o seu nome' or 'qual é seu nome':
        tts.speak(random.choice(answers.MYNAME))

# ASR - Automated Speech Recognition
WAKEUP = ["Stiles", "Stylus", "Stairs"]

while True:
    text = asr.listen()
    print(text)
    for item in WAKEUP:
        if text.count(item) > 0:
            tts.speak(random.choice(answers.TAKECOMMAND))

            print("Escutando...")
            text = asr.listen()
            print(text)
            executeCommand(text)