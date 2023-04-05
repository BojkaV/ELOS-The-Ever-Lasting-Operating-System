from time import sleep
import platform
import os

if platform.system() == 'Windows':
    clear = "cls"
    os.system(clear)
else:
    clear = 'clear'
    os.system(clear)

print("ELOS is starting...")

print("ELOS [Build 1] Ever Lasting Project")
print("(C) ELP ELOS License")

while True:
    commands = []
    com = input('>')

sleep(3)

