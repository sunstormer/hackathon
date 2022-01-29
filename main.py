import sys
import speech_recognition
import pyttsx3 as tts
from trainbot import GenericAssistant, IAssistant

recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 180)

def Greet():
        speaker.say("Hello, how are you?")
        speaker.runAndWait()

def Sad():
        speaker.say("Here is a joke")
        speaker.runAndWait()

def Fear():
        speaker.say("You are stronger than you know")
        speaker.runAndWait()

def Demotivated():
        speaker.say("<insert inspirational quotes>")
        speaker.runAndWait()

def Stress():
        speaker.say("Rome was not built in a day, take a chill pill")
        speaker.runAndWait()

def Exit():
        speaker.say("Bye,have a nice day")
        speaker.runAndWait()
        sys.exit(0)

mappings = {
        "greet": Greet(),
        "leave": Exit(),
        "sad": Sad(),
        "fear": Fear(),
        "demotivated": Demotivated(),
        "stress": Stress(),
}

assistant = GenericAssistant('intents.json', intent_methods= mappings)
assistant.train_model()
assistant.save_model()

while True:
        try:
                with speech_recognition.Microphone() as source:
                        recognizer.energy_threshold = 10000
                        recognizer.adjust_for_ambient_noise(source, duration=0.2)
                        print("listening")
                        audio = recognizer.listen(source)
                        message = recognizer.recognize_google(audio)
                        message = message.lower()
                        print(message)

                assistant.request(message)
        except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
