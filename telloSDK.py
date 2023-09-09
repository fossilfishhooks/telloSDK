# hi
# Tello Python3 Control Demo modified my Arin Jander
#copyright (c) 2023
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time


class telloEDU:
    def __init__(self):
        self.host = ''
        self.port = 9000
        self.locaddr = (self.host,self.port)
        self.out = ""


        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.tello_address = ('192.168.10.1', 8889)

        self.sock.bind(self.locaddr)

    


        #print ('\r\n\r\nTello Python3 Demo.\r\n')

        #print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

        #print ('end -- quit demo.\r\n')


        #recvThread create
        recvThread = threading.Thread(target=self.____recv)
        recvThread.start()
        #self.message('command')
    def ____recv(self):
        count = 0
        while True: 
            try:
                data, server = self.sock.recvfrom(1518)
                print(data.decode(encoding="utf-8"))
                self.out=data.decode(encoding="utf-8")
                #self.out.add(data.encode(encoding="utf-8"))
            except Exception:
                print ('\nExit . . .\n')
                break
    def message(self,msg):
        try:
            if 'end' in msg:
                print ('...')
                self.sock.close()  
                #broeak

            # Send data
            msg = msg.encode(encoding="utf-8") 
            sent = self.sock.sendto(msg, self.tello_address)
        except Exception:
            print("No drone connection")
    def help(self):
        print("See https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf for more quides on commands. If the 'command' doesnt work, it's alredy set.")
    #def takeoff(self):
     #   nessage
    #while True: 

     #   try:
     #       msg = input("UDP:Tello@192.168.10.1:8889> ");

      #      if not msg:
        #        break  

       #     if 'end' in msg:
       #         print ('...')
       #         sock.close()  
       #         break

            # Send data
        #    msg = msg.encode(encoding="utf-8") 
        #    sent = sock.sendto(msg, tello_address)
        #except KeyboardInterrupt:
        #    print ('\n . . .\n')
        #    sock.close()  
        #    break


#example
#import telloSDK as TSDK
#Tello = TSDK.telloEDU()
#Tello.message("battery?")
#print(Tello.out)

