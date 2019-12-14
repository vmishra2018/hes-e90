import picamera
import time
#camera = picamera.PiCamera()
#Setup camera such as it closes when we are done with it.
print("Picture about to be taken")
seconds = time.time()
mypic = open('/home/pi/scripts/images/image_'+str(time)+'.jpg','wb')
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.start_preview()
    #camera warm up time
    time.sleep(2)
    camera.capture(mypic);

mypic.close()
print("picture taken")
