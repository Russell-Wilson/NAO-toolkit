

import sys
import os
from naoqi import ALProxy
from dotenv import load_dotenv

# ENV variables 
load_dotenv()
IP = os.environ.get("IP")
PORT = int(os.environ.get("PORT"))

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(robotIP):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception as e:
        print ("Could not create proxy to ALRobotPosture")
        print ("Error was: ", e)

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception as e:
        print ("Could not create proxy to ALRobotPosture")
        print ("Error was: ", e)


    # Send NAO to Pose Init
    postureProxy.goToPosture("Stand", 1.0)

    # list of additional poses 
    # postureProxy.goToPosture("StandInit", 1.0)
    # postureProxy.goToPosture("SitRelax", 1.0)
    # postureProxy.goToPosture("StandZero", 1.0)
    # postureProxy.goToPosture("LyingBelly", 1.0)
    # postureProxy.goToPosture("LyingBack", 1.0)
    # postureProxy.goToPosture("Stand", 1.0)
    # postureProxy.goToPosture("Crouch", 1.0)
    # postureProxy.goToPosture("Sit", 1.0)

if __name__ == "__main__":

    main(IP)