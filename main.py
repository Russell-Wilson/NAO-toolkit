import os
from dotenv import load_dotenv
from nao import Nao

# ENV variables 
load_dotenv()
IP = os.environ.get("IP")
PORT = int(os.environ.get("PORT"))

# Test functionality
Nao_robot = Nao(IP, PORT)
# Nao_robot.naoSpeech("Nao speech working")
# Nao_robot.naoWalk()
# Nao_robot.naoWalkAndTalk('completed walk')


