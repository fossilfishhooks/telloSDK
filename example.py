import telloSDK as TSDK
import tellostream
import time
Tello = TSDK.telloEDU()
stream = tellostream.TelloStream()

Tello.message('takeoff')
time.sleep(5)
Tello.message('battery?')
#print(Tello.out)
#Tello.message('speed 50')
stream.start()
time.sleep(3)
#time.sleep(1)
#Tello.message('up 10')
time.sleep(1)
Tello.message('forward 30')
time.sleep(5)
for x in range(7):  # go aroung pole
    Tello.message('cw 20')
    time.sleep(2)
    Tello.message('forward 30')
    time.sleep(2)
    Tello.message('back 20')
    time.sleep(2)

Tello.message('land')
stream.end()
Tello.message('end')
