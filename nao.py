from naoqi import ALProxy

class Nao:
  def __init__(self, IP, PORT):
    self.IP = IP
    self.PORT = PORT
    self.memory = ALProxy("ALMemory", self.IP, self.PORT)

  def naoSpeech(self, sentence):
      try: 
        volumproxy = ALProxy("ALAudioDevice", self.IP, self.PORT)
        volumproxy.setOutputVolume(80)
        tts = ALProxy("ALTextToSpeech", self.IP, self.PORT)
        tts.say(sentence)
      except Exception as e: 
        print('could not launch speak', e)

  def naoWalkForward(self):
      try: 
        motion = ALProxy("ALMotion", self.IP, self.PORT)
        motion.moveInit()
        motion.moveTo(0.5, 0, 0)
      except Exception as e: 
        print('could not walk forward', e)

  def naoWalkAndTalk(self, sentence): 
      try: 
        motion = ALProxy("ALMotion", self.IP, self.PORT)
        motion.moveInit()
        travel = motion.post.moveTo(0.5, 0, 0)
        motion.wait(travel, 0)
        self.naoSpeech(sentence)
      except Exception as e: 
        print('could not walk and talk', e)


  
        