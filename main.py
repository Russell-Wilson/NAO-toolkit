import naoqi
import os
from dotenv import load_dotenv

# ENV variables 
load_dotenv()
IP = os.environ.get("IP")
PORT = os.environ.get("PORT")


print(IP)
print('test env')