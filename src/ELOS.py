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

os.system(clear)

print("ELOS 1 [Build 2] Ever Lasting Project")
print("(C) ELP ELOS License")

while True:
    commands = ['help', 'shutdown']
    com = input('> ')
    if com.lower() not in commands:
        print('Invalid Command')
    if com.lower() == 'help':
        print('Here are all available commands:')
        print('help - lists all available commands')
        print('shutdown - shuts down ELOS')
    if com.lower() == 'shutdown':
        os.system(clear)
        print('ELOS is shutting down...')
        sleep(3)
        os.system(clear)
        exit()

sleep(3)

