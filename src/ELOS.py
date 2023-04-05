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
sleep(3)

