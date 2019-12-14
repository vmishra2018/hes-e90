
from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
import picamera
import time
GPIO.setmode(GPIO.BCM)
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('camera')
def takeapicture(status):
    

    #camera = picamera.PiCamera()
    #Setup camera such as it closes when we are done with it.
    print("Picture about to be taken")
    seconds = time.time()
    mypic = open('/home/pi/scripts/images/image_'+str(seconds)+'.jpg','wb')
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.start_preview()
        #camera warm up time
        time.sleep(2)
        camera.capture(mypic);

    mypic.close()
    print("picture taken")

    
    return statement('Picture taken. Thank you.')

@ask.intent('gpio',mapping={'status': 'status'})
def gpio_status(status):

    if status in ['on','high' ]:
      GPIO.setup(21, GPIO.IN)
      state = GPIO.input(21)
      if (state == True):
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21,GPIO.HIGH)
        return statement('Lights are already on')
      else:
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21,GPIO.HIGH)
        return statement('Turning lights {}'.format(status))

    if status in ['off','low' ]:
      GPIO.setup(21, GPIO.IN)
      state = GPIO.input(21)
      print('status of light',state)
      if (state == False):
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21,GPIO.LOW)
        return statement('Lights are already off')
      else:
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21,GPIO.LOW)
        return statement('Turning lights {}'.format(status))



if __name__ == '__main__':
  port = 5000 #the custom port you want
  app.run(host='0.0.0.0', port=port)





