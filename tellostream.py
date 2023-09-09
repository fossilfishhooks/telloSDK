
import subprocess

class TelloStream:
    def __init__(self):
        self.process = None

    def start(self):
       command = ['ffplay.exe', 'udp://0.0.0.0:11111']
       self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)
    def end(self):
        self.process.kill()
