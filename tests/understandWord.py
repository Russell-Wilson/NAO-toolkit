from naoqi import ALProxy
import os
import time
from dotenv import load_dotenv
from nao import Nao

# ENV variables 
load_dotenv()
IP = os.environ.get("IP")
PORT = int(os.environ.get("PORT"))


def getWord():
    data=[]
    asr = ALProxy("ALSpeechRecognition", IP, 9559)

    asr.pause(True)
    asr.setLanguage("English")

    vocabulary = [
        "hello", 
        "no", 
        "please",
        "Thanks", 
        "today",
        "nao",
        "yep"
    ]

    asr.setVocabulary(vocabulary, False)
    asr.subscribe(IP)

    memProxy = ALProxy("ALMemory", IP, 9559)
    memProxy.subscribeToEvent('WordRecognized', IP,'wordRecognized')

    asr.pause(False)

    time.sleep(4)

    asr.unsubscribe(IP)
    data=memProxy.getData("WordRecognized")
    print( "data: %s" % data )
    return data


robot = Nao(IP, PORT)
active = True
while active: 
    try:
        data = getWord()
        robot.naoSpeech("Did you say {}".format(data[0]))
        userInput = raw_input('Enter y or n')
        if userInput == 'y' or userInput == 'q': 
            robot.naoSpeech("Great, bye")
            active = False
        elif userInput == 'n':
            robot.naoSpeech("Trying again")
    except Exception as e:
        print('Listen to word failed', e)





