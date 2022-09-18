from naoqi import ALProxy
from PIL import Image

class Nao:
  def __init__(self, IP, PORT):
    self.IP = IP
    self.PORT = PORT

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
  
  def showNaoImage(self):
    try: 
      camProxy = ALProxy("ALVideoDevice", self.IP, self.PORT)

      resolution = 2    # VGA
      colorSpace = 11   # RGB

      videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
      naoImage = camProxy.getImageRemote(videoClient)
      camProxy.unsubscribe(videoClient)

      # Get the image size and pixel array.
      imageWidth = naoImage[0]
      imageHeight = naoImage[1]
      array = naoImage[6]

      # Create a PIL Image from our pixel array.
      im = Image.frombytes("RGB", (imageWidth, imageHeight), array)

      # Save the image.
      im.save("images\\camImage.png", "PNG")
    except Exception as e:
      print('could not get image', e)


  
        