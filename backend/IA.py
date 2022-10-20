import asyncio
from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string
import json
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

class Model:

    def __init__(self, model_path: str) -> None:
        self.agent = Agent.load(model_path)
        print("NLU model loaded")


    def message(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))
        return json_to_string(result)

mdl = Model(os.getenv('MODEL_PATH'))

def  evaluateIntent(utterance):
    intent = mdl.message(utterance)
    intent = json.loads(intent)
    goal = intent["intent"]["name"]

    features = []
    currentFeature = {}
    for item in intent["entities"]:
        currentFeature["name"] = item["entity"]
        currentFeature["value"] = item["value"]
        features.append(currentFeature)

    print(f"goal: {goal}")
    print(f"feature: {features}")
    intent = {'goal': goal, 'features': features}
    return intent
