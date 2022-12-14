import sys
import os
import motion
from naoqi import ALProxy
from dotenv import load_dotenv

# ENV variables 
load_dotenv()
IP = os.environ.get("IP")
PORT =  int(os.environ.get("PORT"))


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
        print ("Could not create proxy to ALMotion")
        print ("Error was: ", e)

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception as e:
        print ("Could not create proxy to ALRobotPosture")
        print ("Error was: ", e)

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

if __name__ == "__main__":

    main(IP)