
import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser
import os
from dotenv import load_dotenv

# ENV variables 
load_dotenv()
NAO_IP = os.environ.get("IP")
PORT = int(os.environ.get("PORT"))

# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None
Loop = True

class HumanGreeterModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")

        # Subscribe to the FaceDetected event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("FaceDetected",
            "HumanGreeter",
            "onFaceDetected")

    def onFaceDetected(self, *_args):
        memory.unsubscribeToEvent("FaceDetected", "HumanGreeter")
        self.tts.say("Face detected")
        global Loop
        Loop = False
        
def main():

    myBroker = ALBroker("myBroker", "0.0.0.0", 0, "192.168.0.60", 9559)

    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")
  
    
    global Loop
    while Loop:
        time.sleep(1)

    sys.exit('Exited')


if __name__ == "__main__":
    main()